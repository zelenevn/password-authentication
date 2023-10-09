package internal

import (
	"fmt"
	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
	"io"
)

func FrequentDict(L uint, alphabet string, iterations uint) []freqValue {
	var passwords []string

	gen := New(alphabet)
	for i := uint(0); i < iterations; i++ {
		pw := gen.String(int(L))
		passwords = append(passwords, pw)
	}

	dict := make(map[rune]uint)
	for _, key := range alphabet {
		dict[key] = 0
	}
	for _, pw := range passwords {
		for _, letter := range pw {
			dict[letter]++
		}
	}

	var result []freqValue
	for key, value := range dict {
		result = append(result, freqValue{
			letter: key,
			count:  value,
		})
		fmt.Println(string(key), value)
	}

	al := len(alphabet)
	for i := 1; i < al; {
		if result[i].letter < result[i-1].letter {
			result[i], result[i-1] = result[i-1], result[i]
			if i > 1 {
				i--
			}
		} else {
			i++
		}
	}

	return result
}

func OutputToHtml(result []freqValue, f io.Writer) {
	items := make([]opts.BarData, 0)
	var labels []string
	for _, val := range result {
		items = append(items, opts.BarData{Value: val.count, Name: string(val.letter)})
		labels = append(labels, string(val.letter))
	}

	bar := charts.NewBar()
	bar.SetGlobalOptions(charts.WithTitleOpts(opts.Title{
		Title: "Частотный список вхождений символов в пароль",
	}))
	bar.SetXAxis(labels)
	bar.AddSeries("", items)
	_ = bar.Render(f)
}

type freqValue struct {
	letter rune
	count  uint
}

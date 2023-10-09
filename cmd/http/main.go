package main

import (
	"log"
	"net/http"
	"pw-auth/internal"
	"strconv"
)

func main() {

	http.Handle("/", http.FileServer(http.Dir("./resources")))

	http.HandleFunc("/app", func(writer http.ResponseWriter, request *http.Request) {
		if err := request.ParseForm(); err != nil {
			writer.WriteHeader(502)
			return
		}
		length, err := strconv.ParseUint(request.FormValue("length"), 10, 32)
		if err != nil {
			writer.WriteHeader(502)
			return
		}
		count, err := strconv.ParseUint(request.FormValue("count"), 10, 32)
		if err != nil {
			writer.WriteHeader(502)
			return
		}
		iterations, err := strconv.ParseUint(request.FormValue("iterations"), 10, 32)
		if err != nil {
			writer.WriteHeader(502)
			return
		}

		alphabet := internal.LettersLowerCase + internal.Numbers + internal.SpecialChars
		alphabet = alphabet[:count]
		result := internal.FrequentDict(uint(length), alphabet, uint(iterations))

		internal.OutputToHtml(result, writer)
	})

	log.Println("server is starting...")
	if err := http.ListenAndServe(":80", nil); err != nil {
		log.Fatal(err)
	}
}

import unittest
import generator
import logic_service


class TestGenerator(unittest.TestCase):
    generator = generator.PasswordGenerator()

    def test_generator(self):
        password = self.generator.password_generation("abcdefghijklmnopqrstuvwxyz0123456789", 10)
        self.assertTrue(
            password is not None
        )
        self.assertTrue(
            len(password) == 10
        )


class TestLogicService(unittest.TestCase):
    log_serv = logic_service.LogicService()

    def test_num_overlays(self):
        self.assertTrue(
            self.log_serv.get_index(['a', 's', 's', 'd', 'd', 'f', 'f', 'a']) == 3
        )
        self.assertTrue(
            self.log_serv.get_index(
                ['a', 's', 's', 'd', 'd', 'f', 'f', 'a', 'z', 'x', 'x', 'c', 'c', 'v', 'v', 'z']) == 6
        )


if __name__ == '__main__':
    unittest.main()

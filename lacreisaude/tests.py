import datetime

from django.test import TestCase

from .models import Consulta, Profissional


class ProfissionalViewTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(
            nome_social='Maria da Silva',
        )

    def test_get_all_profissionais(self):
        response = self.client.get('http://127.0.0.1:8000/lacreisaude/v1/profissionais')
        self.assertEqual(response.status_code, 200)
    
    def test_post_profissional(self):
        response = self.client.post('http://127.0.0.1:8000/lacreisaude/v1/profissionais',
                                    data={
                                        'nome_social':'Maria da Silva'
                                    })
        self.assertEqual(response.status_code, 201)
    
    def test_get_one_profissional(self):
        response = self.client.get('http://127.0.0.1:8000/lacreisaude/v1/profissionais/1')
        self.assertEqual(response.status_code, 200)


class ConsultaViewTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(
            nome_social='Maria da Silva',
        )

    def test_get_all_consultas(self):
        response = self.client.get('http://127.0.0.1:8000/lacreisaude/v1/consultas')
        self.assertEqual(response.status_code, 200)
    
    def test_post_consulta(self):
        response = self.client.post('http://127.0.0.1:8000/lacreisaude/v1/consultas',
                                    data={
                                        'data_consulta': "2023-12-06T22:16:06.457906Z",
                                        'profissional': 1,
                                    })
        self.assertEqual(response.status_code, 201)

class ProfissionalTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(
            nome_social='Maria da Silva',
        )

    def test_nome_social_retorna_str(self):
        profissional = Profissional.objects.get(nome_social='Maria da Silva')
        self.assertEqual(profissional.__str__(), 'Maria da Silva')

class ConsultaTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(
            nome_social='Maria da Silva',
        )

    def test_post_consulta_com_profissional_existente_retorna_sucesso(self):
        response = self.client.post('http://127.0.0.1:8000/lacreisaude/v1/consultas',
                                    data={
                                        'data_consulta': "2023-12-06T22:16:06.457906Z",
                                        'profissional': 1,
                                    })
        print(response)
        self.assertEqual(response.status_code, 201)
    
    def test_post_consulta_com_profissional_inexistente_retorna_falha(self):
        response = self.client.post('http://127.0.0.1:8000/lacreisaude/v1/consultas',
                                    data={
                                        'data_consulta': "2023-12-06T22:16:06.457906Z",
                                        'profissional': 42,
                                    })
        print(response)
        self.assertEqual(response.status_code, 400)
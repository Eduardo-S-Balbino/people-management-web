import unittest
from unittest.mock import Mock, patch

from app.services.pessoa_service import criar_pessoa, atualizar_pessoa, remover_pessoa


class TestPessoaService(unittest.TestCase):

    @patch("app.services.pessoa_service.db")
    @patch("app.services.pessoa_service.Pessoa")
    def test_criar_pessoa(self, mock_pessoa_class, mock_db):
        mock_nova_pessoa = Mock()
        mock_pessoa_class.return_value = mock_nova_pessoa

        resultado = criar_pessoa("Eduardo", 29)

        mock_pessoa_class.assert_called_once_with(nome="Eduardo", idade=29)
        mock_db.session.add.assert_called_once_with(mock_nova_pessoa)
        mock_db.session.commit.assert_called_once()
        self.assertEqual(resultado, mock_nova_pessoa)

    @patch("app.services.pessoa_service.db")
    def test_atualizar_pessoa(self, mock_db):
        mock_pessoa = Mock()
        mock_pessoa.nome = "Antigo"
        mock_pessoa.idade = 20

        resultado = atualizar_pessoa(mock_pessoa, "Novo Nome", 30)

        self.assertEqual(mock_pessoa.nome, "Novo Nome")
        self.assertEqual(mock_pessoa.idade, 30)
        mock_db.session.commit.assert_called_once()
        self.assertEqual(resultado, mock_pessoa)

    @patch("app.services.pessoa_service.db")
    def test_remover_pessoa(self, mock_db):
        mock_pessoa = Mock()

        remover_pessoa(mock_pessoa)

        mock_db.session.delete.assert_called_once_with(mock_pessoa)
        mock_db.session.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
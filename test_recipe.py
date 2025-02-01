

# test_password_generator.py
import os
from unittest.mock import patch
from recipes import create_random_password, check_password, read_password
import pytest
from dinner import get_dinner
from milkshakes import get_milkshakes

def test_get_dinner_chicken_curry(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_dinner() is None  # Check if it prints the recipe

def test_get_dinner_beef_stew(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert get_dinner() is None  

def test_get_dinner_steak_and_egg(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_dinner() is None  

def test_get_dinner_steak_and_potato(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert get_dinner() is None  

def test_get_dinner_invalid_choice(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    result = get_dinner()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a number from 1 to 4." in captured.out



def test_get_vanilla_shake(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_milkshakes() is None  

def test_get_choclate_shake(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert get_milkshakes() is None  

def test_get_oreo_shake(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_milkshakes() is None  

def test_get_dinner_steak_and_potato(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert get_milkshakes() is None 

def test_get_straberry_shake(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    result = get_milkshakes()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a number from 1 to 4." in captured.out



def test_create_random_password():
    password = create_random_password()
    assert len(password) == 5
    assert os.path.exists("password.txt")
    with open("password.txt", "r") as password_file:
        file_content = password_file.read()
        assert file_content == password
    os.remove("password.txt")

def test_check_password_correct():
    create_random_password()
    
    with patch('builtins.input', return_value=read_password()):
        with patch('builtins.print') as mock_print:
            check_password()
            mock_print.assert_called_with("Password accepted:")
    
    os.remove("password.txt")

def test_check_password_incorrect():
    create_random_password()
    
    with patch('builtins.input', return_value='wrong_password'):
        with patch('builtins.print') as mock_print:
            check_password()
            mock_print.assert_called_with("Incorrect password.")
    
    os.remove("password.txt")





pytest.main(["-v", "--tb=line", "-rN", __file__])

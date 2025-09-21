#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reset do Chatbot FAQ
Autor: André Kroetz Berger
Script para limpar a base de dados e forçar novo treinamento
"""

import os

def reset_chatbot_database():
    """Remove a base de dados para forçar novo treinamento"""
    
    db_files = [
        "notebook_faq.sqlite3",
        "notebook_faq.sqlite3-shm", 
        "notebook_faq.sqlite3-wal"
    ]
    
    print("🔄 RESET DO CHATBOT FAQ")
    print("=" * 40)
    
    removed_count = 0
    
    for db_file in db_files:
        if os.path.exists(db_file):
            try:
                os.remove(db_file)
                print(f"✅ Removido: {db_file}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Erro ao remover {db_file}: {e}")
        else:
            print(f"ℹ️  Não encontrado: {db_file}")
    
    print("-" * 40)
    if removed_count > 0:
        print(f"✅ {removed_count} arquivo(s) removido(s).")
        print("🔄 Execute o chatbot novamente para treinar com as melhorias!")
    else:
        print("ℹ️  Nenhum arquivo de base de dados encontrado.")
    
    print("\n💡 Para executar:")
    print("   python chatbot_faq.py")
    print("   python test_faq.py")

if __name__ == "__main__":
    reset_chatbot_database()

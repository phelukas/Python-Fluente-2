#!/bin/bash

# Mude para o diretório 'Parte-1'
cd Parte-1

# Itera sobre cada arquivo no diretório
for file in *; do
    # Substitui espaços por hifens no nome do arquivo
    new_file=$(echo "$file" | tr ' ' '-')
    
    # Renomeia o arquivo se o nome novo for diferente
    if [ "$file" != "$new_file" ]; then
        mv "$file" "$new_file"
        echo "Renomeando: $file para $new_file"
    fi
done

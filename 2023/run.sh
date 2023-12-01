#!/bin/bash

# Check if a filename is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

filename="$1"

cat << 'EOF'
-------------FUNCTIONAL CHAD----------------
                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \  =  /
                 |\___/|
        ___ ____/:     :\____ ___
      .'   `.-===-\   /-===-.`   '.
     /      .-"""""-.-"""""-.      \
    /'             =:=             '\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   ".     --:--     ."   \_. '\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \
 /... .|      |    |      |      |. ...\
|::::/'' jgs /     |       \     ''\::::|
'""""       /'    .L_      `\       """"'
           /'-.,__/` `\__..-'\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___)
           |==|
           \__/
EOF

if grep -n " = " "$filename"; then
    echo -e "\nWhat's this? Declaring variables again?\nYou're WEAK! And your CODE is WEAK!\n"
    exit 1
else
    echo "\Awesome code. Nice size. Looking thick. Solid. Tight. Keep me posted on your progress.\n"
    python "$filename"
fi
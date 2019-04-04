# Type Conversion
'19'.to_i

'5 hi there'.to_i

'hi there 5'.to_i

'4'.to_f

'4 hi there'.to_f

# Data Structures
# Array
tab = [1, 2, 3, 4, 5, 6]
tab[0]

# Hash
myHash = {:btc => 'bitcoin'}

myHash = {
  :btc => 'bitcoin',
  :eth => 'ethereum',
  :ltc => 'litecoin',
  :bat => 'Basic Attention Token'
}

myHash[:bat]

# Exo
# 1) Ajouter 2 chaînes
# prénom et nom pour pouvoir
# afficher Bonjour prénom nom

# 2) Utiliser % et / pour extraire
# le chiffre des milliers, celui des
# centaines, des dizaines et des
# unités à partir d'un nombre à 4 chiffres
# ex: 2019 => 2, 0, 1, 9

puts "Entrer 1 nombre à 4 chiffres"
nombre = gets.chomp().to_i

chiffres = []

chiffres[0] = nombre / 1000
puts "unité de mille : #{chiffres[0]}"

chiffres[1] = (nombre - chiffres[0] * 1000) / 100
puts "centaine : #{chiffres[1]}"

chiffres[2] = ((nombre - chiffres[0] * 1000) - chiffres[1] * 100) / 10
puts "dizaine : #{chiffres[2]}"

chiffres[3] = (nombre - chiffres[0] * 1000) - chiffres[1] * 100 - chiffres[2] * 10
puts "unité : #{chiffres[3]}"

monHash = {
  :mille => chiffres[0],
  :cent => chiffres[1],
  :dix => chiffres[2],
  :unite => chiffres[3]
}

puts monHash

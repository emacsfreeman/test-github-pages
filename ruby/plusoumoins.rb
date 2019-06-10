# Le bloc des fonctions
def dire_bonjour_et_donner_les_regles
  puts "Bienvenue dans le jeu du plus ou moins !"
  puts "Tu dois trouver le nombre mystère entre 0 et 10"
end

def jouer(nb_a_trouver)
  essais = 1
  proposition = gets.chomp

  while proposition.to_i != nb_a_trouver
    if proposition.to_i < nb_a_trouver
      puts "Plus"
    else
      puts "Moins"
    end
    essais += 1
    proposition = gets.chomp
  end
  return essais
end

# Le corps du programme
dire_bonjour_et_donner_les_regles
nb_a_trouver = rand 10
essais = jouer(nb_a_trouver)

puts "Bravo ! Tu as trouvé en #{essais} coups"

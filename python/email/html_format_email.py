# for Gmail account activate this before https://myaccount.google.com/lesssecureapps?pli=1 
# Useful tutorial: https://youtu.be/JRCJ6RtE3xU

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = 'smtp.gmail.com'
port = 587
username = input('Enter user email: ')
password = input('Enter password: ')
from_email = username

to_list = []
with open('mailin-list.txt', 'r') as list:
    for line in list:
        currentRecipient = line[:-1]
        to_list.append(currentRecipient)

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart('alternative')
    the_msg['Subject'] = 'Quel avenir pour les formations avec ou sans plateforme ?'
    the_msg['From'] = from_email
    # the_msg['To'] = to_list

    plain_txt = 'Testing the message'
    html_txt = """\
    <html>
    <meta charset="utf-8">
    <body>
    <p>Bonjour les gens !</p>

    <p>
    Ceci est un email créé grâce à Python et avec une structure en <a href='https://en.wikipedia.org/wiki/HTML' target='_blank'>HTML</a>.
    </p>
    <p>Normalement, cette fois-ci vous ne devriez pas voir apparaître les adresses mails des autres destinataires.</p>
    <p>Je ne sais pas si vous le savez mais je suis très déçu de la plateforme systeme.io qui devait soi-disant me permettre d'héberger autant de formations que je le souhaite mais en fait les choses sont différentes. Il se trouve que cette plateforme a changé un nombre incalculable de fois son interface.</p>
    <p>Vous savez c'est comme quand vous allez à votre supermarché habituel et qu'ils changent les rayons, vous êtes perdus, vous perdez du temps et cerise sur le gâteau généralement vous vous retrouvez à acheter plus que ce que vous souhaitiez au départ...<br />
     Imaginez la même chose deux à trois fois par mois...</p>
    <p>Bref, in fine comme vous avez pu le constater de toute façon les cours sont hébergés sur mes différentes chaînes YouTube donc finalement quels sont les services que me fournit la plateforme ?</p>
    <ol>
    <li>Gestion des emails (je suis désormais en train de le faire avec Python)</li>
    <li>Pages de présentation des plans des formations (en cours de construction)</li>
    <li>Comptes personnels pour vous (ça c'est plus compliqué à gérer mais pas impossible)</li>
    <li>Interface de paiement automatique en ligne (alternatives possibles)</li>
    </ol>
    <p>
    Pour les mails il me reste juste à gérer l'automatisation et le timing. Concernant les pages de présentation des plans il n'y a aucun problème. Là où ça devient contraignant c'est pour l'authentification et la gestion des données personnelles, à l'heure actuelle je n'ai pas encore trouvé de solution à ce problème. Idem pour l'interface de paiement. Si ce n'est que pour le paiement si on passe par les crypto-monnaies (BTC, ETH, LTC, et <a href='https://youtu.be/U1qbHaLCQNU' target='_blank'>G1 Duniter</a> en font partie) le problème est résolu.<br />
    En effet, au lieu de se connecter à une plateforme tout pourrait être géré par mail et vous auriez accès aux vidéos et aux contenus en pièces jointes des mails. 
    </p>
    <p>Je tiens à vous informer d'ores et déjà que je lance un cycle d'une vidéo par jour sur ma chaîne rebaptisée Computer Code sur laquelle vous pouvez déjà trouver des tutoriels GRATUITS sur <a href='https://www.youtube.com/playlist?list=PLUJNJAesbJGVSyxJrJvvdK5VxzhVYcAXg' target='_blank'>la ligne de commande</a>, <a href='https://www.youtube.com/playlist?list=PLUJNJAesbJGXyh4UjcsQHDXgW1dGRWoRz' target='_blank'>les bases la programation Python</a> et ma <a href='https://www.youtube.com/playlist?list=PLUJNJAesbJGWnAmwCLAv-tJC8S7JwYmTO' target='_blank'>nouvelle série sur Python</a>.</p>
    <p>Pour ce qui est de la suite des formations payantes, je suis en train de préparer une formation avancée en Python que j'ai appelé <strong>Les Recettes de Cuisine au Python (LRCP)</strong> dont voici un aperçu du plan : </p>
    <ol>
    <li>Module 1 : structure de données et algorithmes</li>
    <li>Module 2 : chaînes de caractères et texte</li>
    <li>Module 3 : nombres, dates et temps</li>
    <li>Module 4 : itérateurs et générateurs</li>
    <li>Module 5 : fichiers et E/S</li>
    <li>Module 6 : encodage de données et traitement</li>
    <li>Module 7 : fonctions </li>
    <li>Module 8 : classes et objets</li>
    <li>Module 9 : méta-programmation</li>
    <li>Module 10 : modules et paquets</li>
    <li>Module 11 : réseau et programmation web</li>
    <li>Module 12 : concurrence</li>
    <li>Module 13 : administration système et scripts utilitaires</li>
    <li>Module 14 : tests, débogage, et exceptions</li>
    <li>Module 15 : extensions C</li>
    </ol>
    <p>Je pense que je la démarrerai pour le 1er octobre. Pour ce qui est du prix je pense que je la lancerai à 150€, me contacter en MP sur Telegram si vous êtes intéressé.</p>

    <p>En parallèle je lancerai à partir du 1er octobre le programme <strong>la prépa pour tous</strong> <emph>version informatique</emph>. Il s'agira d'un abonnement sans engagement (à tout moment vous pourrez vous désinscrire). Je suivrais le programme officiel des CPGE disponible <a href='http://cache.media.education.gouv.fr/file/special_3_ESR/50/5/programme-informatique_252505.pdf' target='_blank'>ici</a>. Donc ça signifie qu'il y aura aussi pas mal de maths. Je vous proposerais une vidéo par jour. L'objectif est de faire le programme de la prépa sur au moins les 9 mois scolaires (très probablement 12 parce que nous n'aurons pas les heures disponibles des préparationnaires).</p>
    <p>Concernant le tarif il y a plusieurs options :</p>
    <ul>
    <li>Inscription avant le 1er septembre : 30€ par mois</li>
    <li>Inscription entre le 1er et le 30 septembre : 90€ par mois</li>
    <li>Inscription à partir du 1er octobre : 200€ par mois</li>
    <li>Remise en cas de combo avec la prépa maths :
    <ol>
    <li>Inscription aux 2 formations avant le 1er septembre : 50€ par mois</li>
    <li>Inscription aux 2 formations entre le 1er et le 30 septembre : 170€ par mois</li>
    <li>Inscription aux 2 formations à partir du 1er octobre : 350€ par mois</li>
    </ol>
    </li>
    </ul>
    <p>Pour les maths vous pouvez déjà voir un aperçu du niveau de prépa dans cette <a href='https://www.youtube.com/playlist?list=PLwWStLtwGECZQoLYqBJ7gD9iSOhGnQIC9' target='_blank'>playlist</a> et dans <a href='https://www.youtube.com/playlist?list=PLwWStLtwGECZ1YPIBHzCD3-rzFjCPWnXO' target='_blank'>celle-ci</a> vous pourrez voir de façon imagée un des concepts clés de l'algèbre abstraite. Par contre pour la formation payante il y a aura des exercices du type de la première <a href='https://www.youtube.com/playlist?list=PLwWStLtwGECZQoLYqBJ7gD9iSOhGnQIC9' target='_blank'>playlist</a>. Néanmoins l'objectif est de comprendre pas de se gaver comme des oies pour passer des concours et tout oublier par la suite. Ce qui est hélas le triste sort de la plupart des préparationnaires, ils se gavent de problèmes et autres exercices pour réussir aux concours et après ils sont soit écoeurés soit ont tout simplement oublié tous les concepts fondamentaux étudiés.</p>
    <p>Je terminerai avec la célèbre maxime de Platon : "que nul n'entre ici s'il n'est géomètre". Sauf, que moi je vous propose de le devenir plutôt que de vous exclure parce que vous n'auriez pas eu la bonne idée de l'être.</p>

    <footer>
    <p>Pour les formations que vous pouvez d'ores et déjà acheter en ligne :</p>
    <ul>
        <li>
            Tu veux en savoir plus sur Bitcoin, la Blockchain et les crypto-monnaies ? Alors clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/comment-decouvrir-la-blockchain-sans-se-ruiner">CDBSSR : Comment Découvrir la Blockchain Sans Se Ruiner</a>
        </li>
    
        <li>
            Tu veux apprendre à coder une blockchain avec Python ? Alors clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/apprendre-a-coder-1-blockchain-avec-python">ACBP : Apprends à Coder ta Blockchain avec Python</a>
        </li>
    
        <li>
            Tu veux en savoir plus sur la programmation JavaScript ? Alors clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/javascript-de-0-a-heros">JavaScript de zéro à Héros</a>
        </li>
    
        <li>
            Tu veux en savoir plus sur la programmation Python ? Alors clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/python-de-zero-a-heros">Python de zéro à Héros</a>
        </li>
    </ul>
    
    <p>
        <strong>Pour toute information complémentaire me contacter en MP sur <a href='https://t.me/joinchat/JGxHI1BrJRHC2C0qLtAXYw' target='_blank'>Telegram</a>.</strong></p>
    </footer>
    </body>
    </html>
    """

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)


    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print('Error sending message')

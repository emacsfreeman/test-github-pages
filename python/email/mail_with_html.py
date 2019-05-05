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
    the_msg['Subject'] = 'Comment faire pour aller plus loin avec le code ?'
    the_msg['From'] = from_email
    # the_msg['To'] = to_list

    plain_txt = 'Testing the message'
    html_txt = """\
           <!doctype html>
<html lang="en">
<head>
<title>Computer Code Python CCP 30 : bouquet final</title>
<!-- 2018-09-11 Tue 19:06 -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="Org-mode">
<meta name="author" content="Laurent Garnier">

<link  href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style type="text/css">
/* org mode styles on top of twbs */

html {
    position: relative;
    min-height: 100%;
}

body {
    font-size: 18px;
    margin-bottom: 105px;
}

footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 101px;
    background-color: #f5f5f5;
}

footer > div {
    padding: 10px;
}

footer p {
    margin: 0 0 5px;
    text-align: center;
    font-size: 16px;
}

#table-of-contents {
    margin-top: 20px;
    margin-bottom: 20px;
}

blockquote p {
    font-size: 18px;
}

pre {
    font-size: 16px;
}

.footpara {
    display: inline-block;
}

figcaption {
  font-size: 16px;
  color: #666;
  font-style: italic;
  padding-bottom: 15px;
}

/* from twbs docs */

.bs-docs-sidebar.affix {
    position: static;
}
@media (min-width: 768px) {
    .bs-docs-sidebar {
        padding-left: 20px;
    }
}

/* All levels of nav */
.bs-docs-sidebar .nav > li > a {
    display: block;
    padding: 4px 20px;
    font-size: 14px;
    font-weight: 500;
    color: #999;
}
.bs-docs-sidebar .nav > li > a:hover,
.bs-docs-sidebar .nav > li > a:focus {
    padding-left: 19px;
    color: #A1283B;
    text-decoration: none;
    background-color: transparent;
    border-left: 1px solid #A1283B;
}
.bs-docs-sidebar .nav > .active > a,
.bs-docs-sidebar .nav > .active:hover > a,
.bs-docs-sidebar .nav > .active:focus > a {
    padding-left: 18px;
    font-weight: bold;
    color: #A1283B;
    background-color: transparent;
    border-left: 2px solid #A1283B;
}

/* Nav: second level (shown on .active) */
.bs-docs-sidebar .nav .nav {
    display: none; /* Hide by default, but at >768px, show it */
    padding-bottom: 10px;
}
.bs-docs-sidebar .nav .nav > li > a {
    padding-top: 1px;
    padding-bottom: 1px;
    padding-left: 30px;
    font-size: 12px;
    font-weight: normal;
}
.bs-docs-sidebar .nav .nav > li > a:hover,
.bs-docs-sidebar .nav .nav > li > a:focus {
    padding-left: 29px;
}
.bs-docs-sidebar .nav .nav > .active > a,
.bs-docs-sidebar .nav .nav > .active:hover > a,
.bs-docs-sidebar .nav .nav > .active:focus > a {
    padding-left: 28px;
    font-weight: 500;
}

/* Nav: third level (shown on .active) */
.bs-docs-sidebar .nav .nav .nav {
    padding-bottom: 10px;
}
.bs-docs-sidebar .nav .nav .nav > li > a {
    padding-top: 1px;
    padding-bottom: 1px;
    padding-left: 40px;
    font-size: 12px;
    font-weight: normal;
}
.bs-docs-sidebar .nav .nav .nav > li > a:hover,
.bs-docs-sidebar .nav .nav .nav > li > a:focus {
    padding-left: 39px;
}
.bs-docs-sidebar .nav .nav .nav > .active > a,
.bs-docs-sidebar .nav .nav .nav > .active:hover > a,
.bs-docs-sidebar .nav .nav .nav > .active:focus > a {
    padding-left: 38px;
    font-weight: 500;
}

/* Show and affix the side nav when space allows it */
@media (min-width: 992px) {
    .bs-docs-sidebar .nav > .active > ul {
        display: block;
    }
    /* Widen the fixed sidebar */
    .bs-docs-sidebar.affix,
    .bs-docs-sidebar.affix-bottom {
        width: 213px;
    }
    .bs-docs-sidebar.affix {
        position: fixed; /* Undo the static from mobile first approach */
        top: 20px;
    }
    .bs-docs-sidebar.affix-bottom {
        position: absolute; /* Undo the static from mobile first approach */
    }
    .bs-docs-sidebar.affix .bs-docs-sidenav,.bs-docs-sidebar.affix-bottom .bs-docs-sidenav {
        margin-top: 0;
        margin-bottom: 0
    }
}
@media (min-width: 1200px) {
    /* Widen the fixed sidebar again */
    .bs-docs-sidebar.affix-bottom,
    .bs-docs-sidebar.affix {
        width: 263px;
    }
}
</style>
<script type="text/javascript">
$(function() {
    'use strict';

    $('.bs-docs-sidebar li').first().addClass('active');

    $(document.body).scrollspy({target: '.bs-docs-sidebar'});

    $('.bs-docs-sidebar').affix();
});
</script>
</head>
<body>
<div id="content" class="container">
<div class="row"><div class="col-md-9"><h1 class="title">Computer Code Python CCP 30 : bouquet final</h1>



<div id="outline-container-sec-1" class="outline-2">
<h2 id="sec-1"><span class="section-number-2">1</span> Tes cadeaux GRATUITS</h2>
<div class="outline-text-2" id="text-1">
<ul class="org-ul">
<li>Obtiens GRATUITEMENT ta carte Bitcoin qui te permet de payer comme avec une carte bleue : <a href="https://bit.ly/2QgCLRH">https://bit.ly/2QgCLRH</a>
</li>

<li>Suis-moi sur Steemit parce que tu pourras lire 1 post quotidien
GRATUITEMENT : <a href="https://steemit.com/@lgsp">https://steemit.com/@lgsp</a>
</li>

<li>Extraits GRATUITS de ma formation CDBSSR : <a href="https://goo.gl/Smnoz6">https://goo.gl/Smnoz6</a>
</li>

<li>Extraits GRATUITS de ma formation ACBP : <a href="https://goo.gl/uTQzHA">https://goo.gl/uTQzHA</a>
</li>

<li>Extraits GRATUITS de ma formation FSD : <a href="https://goo.gl/8NC29s">https://goo.gl/8NC29s</a>
</li>
</ul>
</div>
</div>

<div id="outline-container-sec-2" class="outline-2">
<h2 id="sec-2"><span class="section-number-2">2</span> Les témoignages de mes élèves</h2>
<div class="outline-text-2" id="text-2">
<ul class="org-ul">
<li>Fais comme Fanch formes-toi sur les cryptos : <a href="https://youtu.be/lP1xYh7j5xc">https://youtu.be/lP1xYh7j5xc</a>
</li>
<li>Fais comme Deban et investis sur toi-même (et met des écouteurs) :
<a href="https://youtu.be/SuanDrC2EqA">https://youtu.be/SuanDrC2EqA</a>
</li>
<li>Les témoignages sur <a href="https://www.superprof.fr/initiez-langages-programmation-informatique-decouvrir-marche-ordinateur-web.html">Superprof</a>
</li>
</ul>
</div>
</div>

<div id="outline-container-sec-3" class="outline-2">
<h2 id="sec-3"><span class="section-number-2">3</span> Mes offres irrésistibles</h2>
<div class="outline-text-2" id="text-3">
<ul class="org-ul">
<li>Tu veux en savoir plus sur Bitcoin, la Blockchain et les
crypto-monnaies ? Alors clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/comment-decouvrir-la-blockchain-sans-se-ruiner">CDBSSR : Comment Découvrir la Blockchain Sans Se Ruiner</a>
</li>

<li>Tu veux apprendre à coder une blockchain avec Python ? Alors
clique ici et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/apprendre-a-coder-1-blockchain-avec-python">ACBP : Apprends à Coder ta Blockchain avec Python</a>
</li>

<li>Tu veux en savoir plus sur la programmation JavaScript ? Alors clique ici
et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/javascript-de-0-a-heros">JavaScript de zéro à Héros</a>
</li>

<li>Tu veux en savoir plus sur la programmation Python ? Alors clique ici
et inscris-toi à ma formation <a href="https://laurentgarnier.podia.com/python-de-zero-a-heros">Python de zéro à Héros</a>
</li>
</ul>
</div>
</div>

<div id="outline-container-sec-4" class="outline-2">
<h2 id="sec-4"><span class="section-number-2">4</span> Encore des cadeaux GRATUITS</h2>
<div class="outline-text-2" id="text-4">
<ul class="org-ul">
<li>Rejoins mon groupe Telegram pour discuter avec des hommes libres : <a href="https://t.me/joinchat/JGxHI1BrJRHC2C0qLtAXYw">Freemen</a>
</li>
<li>Pour apprendre GRATUITEMENT la ligne de commande clique ici :
<a href="http://bit.ly/2e3WIwT">http://bit.ly/2e3WIwT</a>
</li>
<li>Pour apprendre GRATUITEMENT le mode Org clique là:
<a href="http://bit.ly/2e3VfXq">http://bit.ly/2e3VfXq</a>
</li>
<li>Pour apprendre GRATUITEMENT les commandes Emacs de base clique ici : <a href="http://bit.ly/2hlvXn6">http://bit.ly/2hlvXn6</a>
</li>

<li>Pour apprendre GRATUITEMENT à faire des mathématiques rigoureuses
c'est là : <a href="http://bit.ly/2gzRHua">http://bit.ly/2gzRHua</a>
</li>
<li>Pour apprendre GRATUITEMENT à conserver sa curiosité mathématiques
et s'amuser avec les maths c'est ici : <a href="https://goo.gl/r77fpJ">https://goo.gl/r77fpJ</a> 
</li>
</ul>
</div>
</div>


<div id="outline-container-sec-5" class="outline-2">
<h2 id="sec-5"><span class="section-number-2">5</span> Si tu veux communiquer</h2>
<div class="outline-text-2" id="text-5">
<ul class="org-ul">
<li>Si tu as des suggestions ou que tu souhaites apprendre quelque
chose, laisse un commentaire sous cette vidéo :
<a href="https://youtu.be/eA4HmMxGy-k">https://youtu.be/eA4HmMxGy-k</a>
</li>
<li>Ecris-moi un mail à cours-laurent@tutanota.com et on conviendra
ensemble d'une séance GRATUITE de 30 minutes pour que je réponde à
toutes tes questions
</li>
</ul>
</div>
</div>
</div><div class="col-md-3"><nav id="table-of-contents">
<div id="text-table-of-contents" class="bs-docs-sidebar">
<ul class="nav">
<li><a href="#sec-1">1. Tes cadeaux GRATUITS</a></li>
<li><a href="#sec-2">2. Les témoignages de mes élèves</a></li>
<li><a href="#sec-3">3. Mes offres irrésistibles</a></li>
<li><a href="#sec-4">4. Encore des cadeaux GRATUITS</a></li>
<li><a href="#sec-5">5. Si tu veux communiquer</a></li>
</ul>
</div>
</nav>
</div></div></div>
<footer id="postamble" class="">
<div><p class="author">Author: Laurent Garnier</p>
<p class="date">Created: 2019-05-05 Sun 12:58</p>
<p class="creator"><a href="http://www.gnu.org/software/emacs/">Emacs</a> 25.3.1 (<a href="http://orgmode.org">Org-mode</a> 9.1.6)</p>
</div>
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

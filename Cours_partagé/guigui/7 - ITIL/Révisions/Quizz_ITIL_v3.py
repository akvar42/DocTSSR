import random

questions = [
  "Qu'est-ce que ITIL?",
  "Quelles sont les 5 étapes du cycle de vie des services ITIL?",
  "Qu'est-ce qu'un incident selon ITIL?",
  "Qu'est-ce qu'un problème selon ITIL?",
  "Qu'est-ce que la gestion des niveaux de service selon ITIL?",
  "Quels sont les 5 livres ITIL v3?",
  "A quoi sert le SAC (Service Acceptance Criteria)?",
  "Qu'est-ce que la gestion financière pour ITIL?",
  "Qu'est-ce que la gestion de portefeuille de services?",
  "Qu'est-ce que la gestion des demandes de services?",
  "Qu'est-ce que la gestion des accès selon ITIL?",
  "Quels sont les objectifs clés de la gestion des capacités?",
  "Qu'est-ce que la gestion des configurations selon ITIL?",
  "Qu'est-ce que la gestion des versions et des mises en production?",
  "Qu'est-ce que la gestion du catalogue de services?",
  "Qu'est-ce que le DML (Definitive Media Library)?",
  "Qu'est-ce que la gestion des connaissances?",
  "Qu'est-ce que la gestion des évènements?",
  "Quelle est la différence entre un incident et un problème dans ITIL?",
  "Quels sont les objectifs clés de la gestion des niveaux de service ?",
  "Qu'est-ce que le RACI Matrix en ITIL?",
  "Quelle est l'importance de la gestion des configurations dans ITIL?",
  "Qu'est-ce que la gestion de la continuité des services IT selon ITIL?",
  "Quelles sont les activités principales de la phase de transition dans le cycle de vie des services ITIL?",
  "Qu'est-ce qu'un SLA (Service Level Agreement) en ITIL?",
  "Qu'est-ce que la gestion des fournisseurs en ITIL?",
  "Quelle est la principale responsabilité du Centre de Services en ITIL?",
  "Qu'est-ce que la gestion de la disponibilité selon ITIL?",
  "Quelle est la différence entre le support aux utilisateurs et la gestion des incidents?",
  "Qu'est-ce que la gestion des changements selon ITIL?",
  "Qu'est-ce que le principe de la gestion des services en ITIL?",
  "Quelle est la relation entre ITIL et ISO/IEC 20000?",
  "Qu'est-ce que la gestion de la capacité dans ITIL?",
  "Qu'est-ce que le processus de gestion des problèmes majeurs?",
  "Qu'est-ce que la gestion de la demande en ITIL?",
  "Quels sont les avantages de la mise en œuvre d'ITIL?",
  "Quelle est la phase initiale du cycle de vie des services ITIL?",
  "Qu'est-ce que la gestion des ressources humaines en ITIL?",
  "Qu'est-ce que le processus de gestion des incidents majeurs?",
  "Quels sont les principes de base d'ITIL?",
  "Qu'est-ce que la gestion de la sécurité de l'information en ITIL?"
]


# Choix complets  
choices_list = [
  ["Une norme internationale pour les réseaux","Un framework pour la gestion des services IT","Une méthodologie de développement logiciel","Un outil de monitoring"],
  ["Stratégie, conception, transition, exploitation, amélioration","Planification, construction, vérification, déploiement, fonctionnement","Analyse, conception, développement, test, maintenance","Évaluation, contrôle, surveillance, ajustement"],
  ["Un événement qui cause une interruption non planifiée du service","Une tâche planifiée nécessitant l'arrêt d'un service","Une requête d'assistance de la part d'un utilisateur","Un problème récurrent affectant un service"],
  ["Une cause sous-jacente d'un ou plusieurs incidents","Un incident majeur affectant de nombreux utilisateurs","Une erreur dans la configuration d'un système","Une panne matérielle inattendue"],
  ["La définition des niveaux de qualité de service attendus et mesurables","Le suivi des performances des équipements réseau","La planification de la capacité des infrastructures","La gestion des mises à jour logicielles"],
  ["Stratégie, conception, transition, exploitation, amélioration","Planification, construction, vérification, déploiement, fonctionnement","Analyse, conception, développement, test, maintenance","Évaluation, contrôle, surveillance, ajustement"],
  ["Définit les critères d'acceptation d'un nouveau service ou d'un changement","Spécifie les niveaux de disponibilité et de performance","Documente les configurations autorisées d'un service","Liste les responsabilités des fournisseurs et clients"],
  ["La gestion des coûts et de la facturation des services IT","L'application de la politique financière de l'entreprise","Le contrôle des dépenses d'investissement","L'analyse financière des fournisseurs"],
  ["L'ensemble des services IT gérés par un fournisseur","La liste des services proposés aux clients","Les services prioritaires pour l'entreprise","Les services IT nécessitant un investissement"],
  ["La gestion du cycle de vie des demandes de services des utilisateurs","L'enregistrement et le suivi des incidents","La priorisation des changements et mises en production","L'approbation des accès aux services"],
  ["La gestion des droits d'accès aux services en fonction des rôles","L'authentification des utilisateurs","La sécurisation des réseaux","Le contrôle des accès physiques aux datacenters"],
  ["Aligner la capacité IT avec les besoins métiers","Diminuer les coûts d'infrastructure","Optimiser les ressources et performances","Anticiper la croissance de la demande"],
  ["Maintenir une référence précise des composants des services et de leurs relations","Documenter les architectures techniques","Gérer les versions logicielles","Planifier les changements"],
  ["Coordonner les mises en production et leurs plannings","Valider la conformité des livrables","Gérer les versions des éléments de configuration","Répertorier les logiciels déployés"],
  ["Fournir un catalogue des services disponibles pour les utilisateurs","Établir les contrats de niveau de service (SLA)","Définir les processus ITIL","Inventorier les équipements du datacenter"],
  ["La bibliothèque définitive des médias contenant les versions autorisées","Le référentiel des documentations des services","La base de données des configurations et de leurs relations","Le stockage sécurisé des sauvegardes"],
  ["Partager les bonnes pratiques, l'expertise et l'expérience","Former le personnel IT aux processus","Documenter les services, processus et configurations","Archiver les enregistrements et informations"],
  ["Détecter, logger et notifier les évènements pertinents","Surveiller les performances et la disponibilité","Gérer les alertes de supervision","Analyser les causes premières des incidents"],
  ["Un incident est un dysfonctionnement, un problème est une cause sous-jacente","Un incident affecte un seul utilisateur, un problème affecte plusieurs utilisateurs","Un incident est urgent, un problème ne l'est pas","Un incident est imprévu, un problème est connu"],
  ["Garantir des niveaux de service alignés avec les attentes métier","Limiter le nombre d'incidents","Réduire les coûts de support","Imposer des pénalités financières en cas de non-respect des SLA"],
  ["Matrice définissant les rôles et responsabilités (Responsable, Approbateur, Consulté, Informé)","Liste des changements planifiés et de leurs dates","Synthèse des causes racines des incidents majeurs","Inventaire des composants critiques des services"],
  ["Essentielle pour gérer efficacement les incidents, changements, mises en production, etc.","Obligatoire pour la facturation et la gestion financière","Recommandée pour l'audit et la conformité","Utile pour la gestion des capacités et des performances"],
  ["Assurer le fonctionnement des services critiques suite à un sinistre majeur","Récupérer rapidement après une interruption de service","Empêcher toute interruption de service","Se protéger contre les cyberattaques"],
  ["Planifier et tester les nouveaux services et changements avant déploiement","Former le personnel à l'utilisation des nouveaux services","Communiquer les changements aux utilisateurs","Valider les critères d'acceptation"],
  ["Contrat définissant les niveaux de service attendus et les responsabilités","Licence d'utilisation d'un logiciel","Convention de support technico-fonctionnelle","Accord de confidentialité des données"],
  ["Négocier et gérer les contrats avec les fournisseurs externes","Sélectionner les fournisseurs en fonction de critères objectifs","Imposer des pénalités financières aux fournisseurs en cas de non-respect des engagements","Valider la conformité des services fournis avant paiement"],
  ["Traiter les demandes et incidents, et rétablir le service normal le plus rapidement possible","Développer des solutions technologiques innovantes","Gérer les problèmes et les changements","Définir la stratégie et concevoir les services"],
  ["Optimiser la continuité de service en prévenant et réduisant les interruptions","Mesurer et rapporter la disponibilité des services","Sauvegarder régulièrement les données critiques","Définir les plans de reprise d'activité"],
  ["Le support gère seulement les incidents, la gestion des incidents couvre tout le cycle de vie","Ils sont identiques","Le support assiste les utilisateurs, la gestion des incidents restaure le service","La gestion des incidents concerne uniquement les incidents majeurs"],
  ["Contrôler les changements aux environnements de production pour minimiser les risques","Développer de nouvelles fonctionnalités logicielles","Mettre en production de nouveaux services et changements","Corriger les défaillances et erreurs"],
  ["Fournir de la valeur aux clients en améliorant l'efficacité et l'efficience des services IT","Industrialiser la production des services IT","Réduire les coûts opérationnels","Se conformer aux réglementations et standards"],
  ["ITIL est compatible avec ISO/IEC 20000","ITIL inclut ISO/IEC 20000","ITIL et ISO/IEC 20000 sont en concurrence","ITIL est une marque déposée, ISO/IEC 20000 est une norme internationale"],
  ["S'assurer que les ressources IT sont adéquates pour fournir les services demandés","Ajuster les ressources en fonction des variations cycliques de la charge","Surveiller la utilisation des ressources","Anticiper l'évolution des besoins en capacité"],
  ["Coordonner la gestion des incidents ayant un fort impact","Résoudre les problèmes complexes ou majeurs","Escaler les incidents critiques au management","Déclarer des incidents majeurs et invoquer les procédures d'urgence"],
  ["Comprendre et influencer la demande des utilisateurs pour les services IT","Gérer le pipeline des projets IT","Traiter les demandes entrantes des utilisateurs","Vendre les services du catalogue aux clients internes"],
  ["Amélioration de la qualité et de la continuité des services","Réduction des coûts opérationnels","Accélération du time-to-market","Conformité avec les standards et réglementations"],
  ["Stratégie","Conception","Transition","Exploitation"],
  ["Recruter, former et motiver les équipes IT","Définir les rôles, responsabilités et compétences nécessaires","Gérer les carrières, rémunérations et avantages sociaux","Mesurer la productivité du personnel"],
  ["Coordonner la gestion des incidents ayant un fort impact","Résoudre les problèmes complexes ou majeurs","Escaler les incidents critiques au management","Déclarer des incidents majeurs et invoquer les procédures d'urgence"],
  ["Focus client, globalité, amélioration continue, approche processus, efficacité","Planifier, construire, exécuter, contrôler, s'améliorer","Évaluer, diagnostiquer, soigner, contrôler, accompagner","Collecter, stocker, traiter, analyser, restituer"],
  ["Protéger la confidentialité, l'intégrité et la disponibilité des données et services","Sensibiliser les utilisateurs aux bonnes pratiques de sécurité","Contrôler les accès et prévenir les intrusions","Analyser les risques, détecter et investiguer les incidents de sécurité"]
]

answers = [
  "Une norme internationale pour les réseaux",
  "Stratégie, conception, transition, exploitation, amélioration",
  "Un événement qui cause une interruption non planifiée du service",
  "Une cause sous-jacente d'un ou plusieurs incidents",
  "La définition des niveaux de qualité de service attendus et mesurables",
  "Stratégie, conception, transition, exploitation, amélioration",
  "Définit les critères d'acceptation d'un nouveau service ou d'un changement",
  "La gestion des coûts et de la facturation des services IT",
  "L'ensemble des services IT gérés par un fournisseur",
  "La gestion du cycle de vie des demandes de services des utilisateurs",
  "La gestion des droits d'accès aux services en fonction des rôles",
  "Aligner la capacité IT avec les besoins métiers",
  "Maintenir une référence précise des composants des services et de leurs relations",
  "Coordonner les mises en production et leurs plannings",
  "Fournir un catalogue des services disponibles pour les utilisateurs",
  "La bibliothèque définitive des médias contenant les versions autorisées",
  "Partager les bonnes pratiques, l'expertise et l'expérience", 
  "Détecter, logger et notifier les évènements pertinents",
  "Un incident est un dysfonctionnement, un problème est une cause sous-jacente",
  "Garantir des niveaux de service alignés avec les attentes métier",
  "Matrice définissant les rôles et responsabilités (Responsable, Approbateur, Consulté, Informé)",
  "Essentielle pour gérer efficacement les incidents, changements, mises en production, etc.",
  "Assurer le fonctionnement des services critiques suite à un sinistre majeur",
  "Planifier et tester les nouveaux services et changements avant déploiement",
  "Contrat définissant les niveaux de service attendus et les responsabilités",
  "Négocier et gérer les contrats avec les fournisseurs externes",
  "Traiter les demandes et incidents, et rétablir le service normal le plus rapidement possible",
  "Optimiser la continuité de service en prévenant et réduisant les interruptions",
  "Le support gère seulement les incidents, la gestion des incidents couvre tout le cycle de vie",
  "Contrôler les changements aux environnements de production pour minimiser les risques",
  "Fournir de la valeur aux clients en améliorant l'efficacité et l'efficience des services IT",
  "ITIL est compatible avec ISO/IEC 20000",
  "S'assurer que les ressources IT sont adéquates pour fournir les services demandés",
  "Coordonner la gestion des incidents ayant un fort impact",
  "Comprendre et influencer la demande des utilisateurs pour les services IT",
  "Amélioration de la qualité et de la continuité des services",
  "Stratégie",
  "Recruter, former et motiver les équipes IT",
  "Coordonner la gestion des incidents ayant un fort impact",
  "Focus client, globalité, amélioration continue, approche processus, efficacité",
  "Protéger la confidentialité, l'intégrité et la disponibilité des données et services"
]

# Initialiser un pool de questions/choix non posées
remaining_questions = list(range(len(questions)))

score = 0 

print("Bienvenue dans le quizz ITIL !")
print("41 questions... à vous de jouer !")
print("Votre score sera affiché à la fin")
print("C'est parti !")
print("---------------------------------")

while remaining_questions:

  # Tirer aléatoirement une question non posée
  q_index = random.choice(remaining_questions)  
  remaining_questions.remove(q_index)
  
  question = questions[q_index]
  choices = choices_list[q_index]
  
  # Poser la question
  print(question)

  # Mélanger les choix
  random.shuffle(choices)

  for i, choice in enumerate(choices):
    print(f"{i+1}) {choice}")

  # Demander la réponse    
  answer = input("Votre réponse (numéro): ")
  student_answer = choices[int(answer)-1]

  # Vérifier et compter points
  if student_answer == answers[q_index]:
      print("Bonne réponse!\n")
      score += 1
  else:
      print(f"Mauvaise réponse. La bonne réponse est {answers[q_index]}.\n")

print(f"Votre score est de {score}/{len(questions)}")
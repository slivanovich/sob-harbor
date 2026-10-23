{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Marriage of Figaro: The Marriage of Figaro (Italian: Le nozze di Figaro , ] ), K. 492, is an opera buffa (comic opera) in four acts composed in 1786 by Wolfgang Amadeus Mozart, with an Italian libretto written by Lorenzo Da Ponte.  It premiered at the Burgtheater in Vienna on 1 May 1786.  The opera's libretto is based on a stage comedy by Pierre Beaumarchais, \"La folle journée, ou le Mariage de Figaro\" (\"The Mad Day, or The Marriage of Figaro\"), which was first performed in 1784.  It tells how the servants Figaro and Susanna succeed in getting married, foiling the efforts of their philandering employer Count Almaviva to seduce Susanna and teaching him a lesson in fidelity.\n\nTosca: Tosca (] ) is an opera in three acts by Giacomo Puccini to an Italian libretto by Luigi Illica and Giuseppe Giacosa.  It premiered at the Teatro Costanzi in Rome on 14 January 1900.  The work, based on Victorien Sardou's 1887 French-language dramatic play, \"La Tosca\", is a melodramatic piece set in Rome in June 1800, with the Kingdom of Naples's control of Rome threatened by Napoleon's invasion of Italy.  It contains depictions of torture, murder and suicide, as well as some of Puccini's best-known lyrical arias.\n\nDubrovsky (opera): Dubrovsky (Russian: \"Дубровский\" ) is an opera in four acts (5 scenes) Op. 58, by Eduard Nápravník, to a Russian libretto by Modest Ilyich Tchaikovsky after the novel of the same title (1832) by Alexander Pushkin.\n\nLa Gioconda (opera): La Gioconda is an opera in four acts by Amilcare Ponchielli set to an Italian libretto by Arrigo Boito (as Tobia Gorrio), based on \"Angelo, Tyrant of Padua\", a play in prose by Victor Hugo, dating from 1835.  (This is the same source as Gaetano Rossi had used for his libretto for Mercadante's \"Il giuramento\" in 1837).\n\nNabucco: Nabucco (] ; short for Nabucodonosor ] ~] , English Nebuchadnezzar) is an Italian-language opera in four acts composed in 1841 by Giuseppe Verdi to an Italian libretto by Temistocle Solera.  The libretto is based on biblical books of Jeremiah and Daniel and the 1836 play by Auguste Anicet-Bourgeois and Francis Cornue, although Antonio Cortese's ballet adaptation of the play (with its necessary simplifications), given at La Scala in 1836, was a more important source for Solera than the play itself.  Under its original name of \"Nabucodonosor\", the opera was first performed at La Scala in Milan on 9 March 1842.\n\nA Life for the Tsar: A Life for the Tsar (Russian: Жизнь за царя , \"Zhizn' za tsarya\"), as it is known in English, although in Soviet times its name was \"Ivan Susanin\" (Russian: Иван Сусанин ) is a \"patriotic-heroic tragic opera\" in four acts with an epilogue by Mikhail Glinka.  The original Russian libretto, based on historical events, was written by Nestor Kukolnik, Egor Fyodorovich (von) Rozen, Vladimir Sollogub and Vasily Zhukovsky.  It premiered on 27 November 1836 OS (9 December NS) at the Bolshoi Kamenny Theatre in St. Petersburg.  The historical basis of the plot involves Ivan Susanin, a patriotic hero of the early 17th century who gave his life in the expulsion of the invading Polish army for the newly elected Tsar Mikhail, the first of the Romanov dynasty, elected in 1613.\n\nL'arlesiana: L'arlesiana is an opera in three acts by Francesco Cilea to an Italian libretto by Leopoldo Marenco.  It was originally written in four acts, and was first performed on 27 November 1897 at the Teatro Lirico di Milano in Milan.  It was revised as a three-act opera in 1898, and a prelude was added in 1937.\n\nThe Gambler (Prokofiev): The Gambler (Russian: Игрок — \"Igrok\" in transliteration) is an opera in four acts by Sergei Prokofiev to a Russian libretto by the composer, based on the story of the same name by Fyodor Dostoyevsky.\n\nThe Snow Maiden: The Snow Maiden (subtitle: A Spring Fairy Tale) (Russian: Снегурочка–Весенняя сказка , \"Snegúrochka–Vesennyaya Skazka\") is an opera in four acts with a prologue by Nikolai Rimsky-Korsakov, composed during 1880–1881.  The Russian libretto, by the composer, is based on the like-named play by Alexander Ostrovsky (which had premiered in 1873 with incidental music by Tchaikovsky).\n\nRusalka (Dargomyzhsky): Rusalka (Russian: Руса́лка ) is an opera in four acts, six tableaux, by Alexander Dargomyzhsky, composed during 1848-1855.  The Russian libretto was adapted by the composer from Pushkin's incomplete dramatic poem of the same name.  It premiered on 4 May 1856 (Old Style) at the Theatre-circus, conducted by Konstantin Lyadov (father of Anatoly Lyadov), choreographed by Marius Petipa and Nikolay Goltz, but was badly received predominantly by the aristocracy.\n\nQuestion: A Life for the Tsar is a  Russian libretto with four acts, Tosca an Italian libretto has how many acts?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opera_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the opera.\"\n    },\n    \"composer\": {\n      \"type\": \"string\",\n      \"description\": \"The composer of the opera.\"\n    },\n    \"libretto_language\": {\n      \"type\": \"string\",\n      \"description\": \"The language of the opera's libretto.\"\n    },\n    \"number_of_acts\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of acts in the opera.\"\n    }\n  },\n  \"required\": [\n    \"opera_name\",\n    \"composer\",\n    \"libretto_language\",\n    \"number_of_acts\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opera_name": {
        "type": "string",
        "description": "The name of the opera."
      },
      "composer": {
        "type": "string",
        "description": "The composer of the opera."
      },
      "libretto_language": {
        "type": "string",
        "description": "The language of the opera's libretto."
      },
      "number_of_acts": {
        "type": "integer",
        "description": "The total number of acts in the opera."
      }
    },
    "required": [
      "opera_name",
      "composer",
      "libretto_language",
      "number_of_acts"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

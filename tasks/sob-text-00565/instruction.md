{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDeathcrush: Deathcrush is an EP by the Norwegian black metal band Mayhem.  It was released on 16 August 1987 by the Posercorpse record label, and was the first studio release by any band in the Norwegian black metal scene.\n\nBurzum: Burzum ( ; ] ) is a music project that began in 1991 by the Norwegian musician and writer Varg Vikernes.  It became a part of the early Norwegian black metal scene and is considered to be one of the most influential acts in black metal.\n\nThou Shalt Suffer: Thou Shalt Suffer were a band that was part of the early Norwegian black metal scene.  It formed in 1990 at Akkerhaugen, Norway, under the name \"Dark Device\".  Its style was mainly death metal, though it included some black metal traits, alongside Ihsahn's trademark keyboard melodies.  The band split up in late 1991 when its members formed Emperor and Ildjarn.\n\nPure Fucking Mayhem: Pure Fucking Mayhem is a 2008 documentary created by Stefan Rydehed which gives an inside look at the second wave Norwegian black metal band, Mayhem.  The movie includes interviews with the band members as well as some previously unseen pictures of the early black metal scene.\n\nEuronymous: Øystein Aarseth (] ; 22 March 1968 – 10 August 1993), who went by the pseudonym Euronymous, was a Norwegian guitarist.  Euronymous was a founder of and central figure in the early Norwegian black metal scene.  He was a co-founder of the Norwegian black metal band Mayhem.  He was also founder and owner of the extreme metal record label Deathlike Silence Productions and record shop Helvete.\n\nThorns (band): Thorns is a Norwegian black metal band that formed in 1989 and was part of the early Norwegian black metal scene.  They made two highly influential demos in the early 1990s, \"Grymyrk\" and \"Trøndertun\", but have only released one full-length album.\n\nMayhem (band): Mayhem is a Norwegian black metal band formed in 1984 in Oslo.  They were one of the founders of the Norwegian black metal scene and their music has strongly influenced the black metal genre.  Mayhem's early career was highly controversial, primarily due to their notorious live performances, the 1991 suicide of vocalist Per Yngve Ohlin (\"Dead\") and the 1993 murder of guitarist Øystein Aarseth (\"Euronymous\") by former member Varg Vikernes (\"Count Grishnackh\"), of Burzum.\n\nDarkthrone: Darkthrone is a Norwegian heavy metal band.  It formed in 1986 as a death metal band under the name Black Death.  In 1991, the band embraced a black metal style influenced by Bathory and Celtic Frost and became one of the leading bands in the Norwegian black metal scene.  Their first three black metal albums—\"A Blaze in the Northern Sky\", \"Under a Funeral Moon\" and \"Transilvanian Hunger\" (sometimes dubbed the \"Unholy Trinity\") — are considered the peak of the band's career and to be among the most influential albums in the genre.  For most of this time, Darkthrone has been a duo of Nocturno Culto and Fenriz, who have sought to remain outside the music mainstream.  Since 2006, their work has strayed from the traditional black metal style and incorporated more elements of traditional heavy metal, speed metal and punk rock, being likened to Motörhead.\n\nParabellum (band): Parabellum were a Colombian extreme metal band from Medellín active in the 1980s.  The band was described by \"Terrorizer\" magazine as one of the world's first black metal bands, as well as the first extreme metal band from Colombia and one of the very first from all South America.  According to writer Emilio Cuesta, Øystein \"Euronymous\" Aarseth—a musician associated with the early Norwegian black metal scene—has said Parabellum and Medellín's Reencarnación were both influential to his own band Mayhem.\n\nFimbulwinter (band): Fimbulwinter was a black metal band that was part of the early Norwegian black metal scene.  It formed in Oslo during 1992 and released two demos that year.  In 1994 it released its only album, \"Servants of Sorcery\".  Featuring a cover of Celtic Frost's \"Morbid Tales\", it was the first release by newly formed Hot Records.\n\nQuestion: Mayhem's lineup changed because of the murder of which founder of the early Norwegian black metal scene?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person.\"\n    },\n    \"pseudonym\": {\n      \"type\": \"string\",\n      \"description\": \"The pseudonym used by the person.\"\n    },\n    \"role_in_mayhem\": {\n      \"type\": \"string\",\n      \"description\": \"The person's role in the band Mayhem.\"\n    },\n    \"role_in_scene\": {\n      \"type\": \"string\",\n      \"description\": \"The person's significance in the early Norwegian black metal scene.\"\n    },\n    \"year_of_death\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the person died.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"pseudonym\",\n    \"role_in_mayhem\",\n    \"role_in_scene\",\n    \"year_of_death\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person."
      },
      "pseudonym": {
        "type": "string",
        "description": "The pseudonym used by the person."
      },
      "role_in_mayhem": {
        "type": "string",
        "description": "The person's role in the band Mayhem."
      },
      "role_in_scene": {
        "type": "string",
        "description": "The person's significance in the early Norwegian black metal scene."
      },
      "year_of_death": {
        "type": "integer",
        "description": "The year the person died."
      }
    },
    "required": [
      "person_name",
      "pseudonym",
      "role_in_mayhem",
      "role_in_scene",
      "year_of_death"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

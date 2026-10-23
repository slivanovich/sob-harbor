{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBeast (comics): Beast (Henry Philip \"Hank\" McCoy) is a fictional superhero appearing in American comic books published by Marvel Comics and is a founding member of the X-Men.  Originally called \"The Beast\", the character was introduced as a mutant possessing ape-like superhuman physical strength and agility, oversize hands and feet, a genius-level intellect, and an otherwise normal appearance.  Eventually being referred to simply as \"Beast\", Hank McCoy underwent progressive physiological transformations, permanently gaining animalistic physical characteristics.  These include blue fur, both simian and feline facial features, pointed ears, fangs, and claws.  Beast's physical strength and senses increased to even greater levels.\n\nBibhuti Bhushan Nayak: Bibhuti Bhushan Nayak (born 1965) is an Indian journalist, who holds seven Guinness World Records and 12 Limca Book Records in physical strength to his name.  He aims to have 72 records to his name.  He currently manages his Ancestral business, works as a journalist at \"The Times of India\" and teaches underprivileged children martial arts to continue the training of breaking world records.  Bibhuti sustains himself on a completely vegetarian diet consisting only of pulses and sprouts.  Nayak graduated as a management student from Osmania University.  In recognition of his physical strength feats he was given an honorary title of \"Singh\" and a pagri (turban) by the Gurudwara where he attempted the record.In addition to that, he is popularly known as the \"Bruce Lee\" of Navi Mumbai, for his martial arts and record breaking accolades.\n\nHulk (comics): The Hulk is a fictional superhero appearing in American comic books published by Marvel Comics.  Created by writer Stan Lee and artist Jack Kirby, the character first appeared in the debut issue of \"The Incredible Hulk\" (May 1962).  In his comic book appearances, the character is both the Hulk, a green-skinned, hulking and muscular humanoid possessing a vast degree of physical strength, and his alter ego Bruce Banner, a physically weak, socially withdrawn, and emotionally reserved physicist, the two existing as personalities independent and resenting of the other.\n\nHulk: Where Monsters Dwell: Hulk: Where Monsters Dwell is a 2016 direct to video animated film featuring the character the Hulk.  The movie takes its name from a 1970s Marvel comic book title.  Just like \"Marvel Super Hero Adventures: Frost Fight\", this film is within the Marvel Animated Universe.\n\nDoctor Cyber: Doctor Cyber is a fictional character appearing in DC Comics publications and related media, traditionally as an adversary of the superhero Wonder Woman.  She first appeared in 1968 as the head of a vast global criminal and terrorist group in \"Wonder Woman\", vol.  1, issue #179, written by Dennis O'Neil and illustrated by Mike Sekowsky and Dick Giordano.  In her early appearances, Dr. Cyber was a beautiful and elegantly-attired woman.  Later, after her face was disfigured in an accident, she donned a gold muzzle-mask and technologically advanced full-body exoskeleton.  These cybernetic enhancements increased Cyber's physical strength, and gave her the ability to absorb and redirect energy, as well as to fire energy blasts from her hands.  Despite the resulting upgrades to her power, Dr. Cyber's disfigurement also wrought a mounting emotional instability.  She became obsessed with recapturing her beauty by transferring her mind into Wonder Woman's body, a project she attempted several times with the help of her operative Doctor Moon.\n\nAerobics: Aerobics is a form of physical exercise that combines rhythmic aerobic exercise with stretching and strength training routines with the goal of improving all elements of fitness (flexibility, muscular strength, and cardio-vascular fitness).  It is usually performed to music and may be practiced in a group setting led by an instructor (fitness professional), although it can be done solo and without musical accompaniment.  With the goal of preventing illness and promoting physical fitness, practitioners perform various routines comprising a number of different dance-like exercises.  Formal aerobics classes are divided into different levels of intensity and complexity.  A well-balanced aerobics class will have five components: warm-up (5–10 minutes), cardio vascular conditioning (25–30 minutes), muscular strength and conditioning (10–15 minutes), cool-down (5–8 minutes) and stretching and flexibility (5–8 minutes).  Aerobics classes may allow participants to select their level of participation according to their fitness level.  Many gyms offer a variety of aerobic classes.  Each class is designed for a certain level of experience and taught by a certified instructor with a specialty area related to their particular class.\n\nMuscular Judaism: Muscular Judaism (German: \"Muskeljudentum\" ) is a term coined by Max Nordau in his speech at the Second Zionist Congress held in Basel on August 28, 1898.  In his speech he spoke about the need to design the \"new Jew\" and reject the \"old Jew\", with the mental and physical strength to achieve the goals of Zionism.  Nordau saw Muscular Judaism as an answer to \"Judennot\" (\"Jewish distress\").\n\nEtrigan the Demon: Etrigan the Demon is a fictional superhero and antihero appearing in comic books published by DC Comics.  Created by Jack Kirby, Etrigan is a demon from Hell who, despite his violent tendencies, usually finds himself allied to the forces of good, mainly because of the alliance between the heroic characters of the DC Universe and Jason Blood, a human to whom Etrigan is bound.  Etrigan is a muscular humanoid creature with orange or yellow skin, horns, red eyes, and pointed, webbed ears.  The character was originally based in Gotham City, leading to numerous team-ups with Batman.\n\nPhysical strength: Physical strength is the measure of an animal's exertion of force on physical objects. Increasing physical strength is the goal of strength training.\n\nMak Yuree: Mak Yuree (Bengali: এমএকে ইউরী ;born 1964) also known as Vajramunee, is a superhuman as seen on Discovery Channel.  He is the founder of Vajrapran and Butthan movement, the South Asian combat sports and system of personal development with the aim to obtain body-mind balance.  He was selected and featured as one of the top five superhuman of the planet in strength category by a team of scientists of Discovery Channel in 2013.  Yuree is cited as 'one of the world’s most unique martial artists, a foremost authority in the field of mind training, meditation, motivational speaking and art of self-defense.'  He is a Bangladeshi born Grandmaster, known for his extraordinary ability to engage highest percentage (96%) of muscles in the world through meditation.  He is a 10th degree black belt holder and the President of the World Combat Self Defense Federation and Secretary General of International Butthan Federation.  He went on to become the Grandmaster of the year 2007 at World Martial Arts Hall of Fame.  He advocates spiritual enlightenment through cultivating physical strength and mindfulness in balance.  He is also known as The Thunder Shin Man.\n\nQuestion: Which 2016 animated film featured a green-skinned, hulking and muscular humanoid possessing a vast degree of physical strength?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the animated film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"featured_character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the featured character.\"\n        },\n        \"physical_attributes\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key physical characteristics of the character.\"\n        },\n        \"abilities\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Special abilities of the character.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"physical_attributes\",\n        \"abilities\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"featured_character\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the animated film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "featured_character": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the featured character."
          },
          "physical_attributes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key physical characteristics of the character."
          },
          "abilities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Special abilities of the character."
          }
        },
        "required": [
          "name",
          "physical_attributes",
          "abilities"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "featured_character"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

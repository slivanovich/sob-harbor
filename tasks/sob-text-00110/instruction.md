{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMeena Bazaar (Karimabad): Meena Bazar is a bazaar located in Karimabad area of Gulberg Town in Karachi, Sindh, Pakistan.  It is a woman-centered shopping street with ladies wear, fashion shops for ladies, restaurants and with a few men's wear shops.  It also has many mehndi or henna shops for dyeing ladies' hands for special occasions like wedding events and 'Eid'.  Meena Bazaar is also popular among tourists looking for locations of cultural interest in Karachi.\n\nClaude Rifat: Claude Rifat (1 March 1952, Cairo - July 31, 2002) was a French biologist, psychonaut, political activist, writer, and researcher.  His accomplishments include some early research into GHB, including the thymoanaleptic/antidepressant and sociabilising effects of this molecule.  He is credited with providing the first live plant material and seeds of Mitragyna speciosa outside Thailand, including several bioassays.  This material is the source of the vast majority of Kratom plants currently available outside Thailand.\n\nMuddu Meena: Muddu Meena (Kannada: ಮುದ್ದು ಮೀನ) is a 1967 Indian Kannada film, directed by Y. R. Swamy and produced by S Heerabai.  The film stars Kalyan Kumar, Jayanthi, K. S. Ashwath and Narasimharaju in lead roles.  The film had musical score by G. K. Venkatesh and Upendra Kumar.\n\nTales of Mobile: Tales of Mobile (テイルズオブモバイル , Teiruzu Obu Mobairu ) is the collective name of several mobile phone-based games available only to Japanese NTT DoCoMo FOMA 900i cellphone users that often feature characters and story elements from the popular \"Tales\" role-playing video game series.  As these games are offered as a download-only phone service in Japan, none of them has been made available outside Japan.\n\nCinema of India: The cinema of India also known by its sobriquet Indywood consists of films produced across India.  Cinema has immense popularity in the country.  As many as 1,600 films in various languages of India are produced every year.  Indian films have also wide following throughout the rest of South Asia and it is even available in mainstream cinemas in parts of the Greater Middle East, Southeast Asia, Eastern Africa and elsewhere.  Dadasaheb Phalke is known as the \"father of Indian cinema\".  The Dadasaheb Phalke Award, for lifetime contribution to cinema, was instituted in his honour, by the Government of India in 1969, and is the most prestigious and coveted award in Indian cinema.\n\nInterstate Migrant Workmen Act 1979: The Inter-State Migrant Workmen (Regulation of Employment and Conditions of Service) Act, 1979 is an Act of the Parliament of India enacted to regulate the condition of service of inter-state labourers in Indian labour law.  The Act's purpose is to protect workers whose services are requisitioned outside their native states in India.  Whenever an employer faces shortage of skills among the locally available workers, the act creates provision to employ better skilled workers available outside the state.\n\nRusty Knife: Rusty Knife (錆びたナイフ Sabita naifu) is a 1958 action Japanese film directed by Toshio Masuda.  \"Rusty Knife\" was part of the Nikkatsu film studio's wave of Japanese \"noir\" films, made in order to compete with popular American and French films at the Japanese box office.  The film became more widely available outside Japan only when Janus Films released a special set of Nikkatsu \"noir\" films on DVD, as part of the Criterion Collection.  The other films in the set are \"A Colt Is My Passport\", \"Take Aim at the Police Van\", \"Cruel Gun Story\", and \"I Am Waiting\".\n\nBoca Burger: Boca Burger is a veggie burger made chiefly from soy protein and wheat gluten; it is a registered trademark of the Boca Foods Company, a subsidiary of Kraft Foods.  Like all of Boca Foods' products, Boca Burgers serve as a meat analogue.  Although most of Boca products are vegetarian and may include animal-derived ingredients such as dairy products, some of them are vegan.  As of summer 2008, Boca Burgers are not available outside North America, and there are no current plans to offer them internationally.\n\nSudhakar Bokade: Sudhakar Bokade was an Indian film producer predominantly working in Bollywood film industry.  He produced popular films like \"\" (1991), \"Saajan\" (1991), \"Dhanwaan\" (1993) and more.  He was considered as a \"big name\" in mid-1990s in the Bollywood film industry.\n\nHeadlines! Live from the Hammersmith Apollo: Headlines!  Live from the Hammersmith Apollo is the first live DVD by British girl group The Saturdays.  The DVD was filmed on 17 February 2011 when the band performed at the Hammersmith Apollo during their The Headlines Tour.  The DVD was released as a bonus as part of the deluxe boxset of the band's third album \"On Your Radar\".  The DVD is not available outside the boxset, and the boxset was only available for purchase from the band's official store on Universal Music.\n\nQuestion: Where else are popular films like Muddu Meena available outside of India?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the film was produced.\"\n    },\n    \"availability_outside_origin\": {\n      \"type\": \"array\",\n      \"description\": \"A list of regions where the film, or films from its country of origin, are available.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"is_widely_available\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if films from the country of origin have a wide following internationally.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"country_of_origin\",\n    \"availability_outside_origin\",\n    \"is_widely_available\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the film was produced."
      },
      "availability_outside_origin": {
        "type": "array",
        "description": "A list of regions where the film, or films from its country of origin, are available.",
        "items": {
          "type": "string"
        }
      },
      "is_widely_available": {
        "type": "boolean",
        "description": "Indicates if films from the country of origin have a wide following internationally."
      }
    },
    "required": [
      "film_title",
      "country_of_origin",
      "availability_outside_origin",
      "is_widely_available"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

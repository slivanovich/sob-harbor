{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJ. Roger Hindley: J. Roger Hindley is a prominent British logician best known for the Hindley–Milner type inference algorithm.  Since 1998, he has been an Honorary Research Fellow at Swansea University.\n\nRoger Batzel: Roger Elwood Batzel (December 1, 1921 – July 29, 2000) was an American nuclear scientist, best known as the director of the Lawrence Livermore National Laboratory for over sixteen years, from 1971 to 1988.\n\nRoger Hanin: Roger Hanin (born Roger Levy, 20 October 1925 – 11 February 2015) was a French actor and film director, best known for playing the title role in the 1989–2006 TV police drama, \"Navarro\".\n\nRoger Webb: Roger Webb (7 April 1934 in Bristol – 19 December 2002 in London) was a British songwriter and jazz pianist best known for leading Roger Webb's Trio (1964–65) for television series and club performances, and Roger Webb's Orchestra.\n\nCharles Fleischer: Charles Fleischer (born August 27, 1950) is an American stand-up comedian, actor, voice actor, writer and musician, best known for appearing in films such as \"A Nightmare on Elm Street\", \"Who Framed Roger Rabbit\", \"Back to the Future Part II\", \"The Polar Express\", \"Rango\", and \"We're Back!  A Dinosaur's Story\".  He also reprised the role of Roger Rabbit in the \"Roger Rabbit\" theatrical shorts.  After beginning his career on the comedy club circuit, Charles Fleischer's first big break in comedy television came when he made an appearance on \"Rowan & Martin's Laugh-In\".\n\nJemdet Nasr: Jemdet Nasr (Arabic: جمدة نصر‎ ‎ ) is a tell or settlement mound in Babil Governorate (Iraq) that is best known as the eponymous type site for the Jemdet Nasr period (3100–2900 BC).  The site was first excavated in 1926 by Stephen Langdon, who found proto-cuneiform clay tablets in a large mudbrick building thought to be the ancient administrative centre of the site.  A second season took place in 1928, but this season was very poorly recorded.  Subsequent excavations in the 1980s under British archaeologist Roger Matthews were, among other things, undertaken to relocate the building excavated by Langdon.  These excavations have shown that the site was also occupied during the Ubaid, Uruk and Early Dynastic I periods.\n\nSara Soskolne: Sara Soskolne (born 1970) is a Canadian type designer best known for her work at Hoefler & Frere-Jones (H&FJ) type foundry on typefaces such as Gotham.  After ten years working in graphic design in Toronto, Soskolne attended the University of Reading where she received her MA in 2003.  She has taught type design at Yale School of Art, the Book Arts Institute at Wells College, and New York’s School of Visual Arts and the Cooper Type Certificate Program.  Soskolne has written about the evolution of sans-serif lower case types in the 19th century.\n\nFonderie Olive: The Fonderie Olive, in English, Olive Foundry, was a small but high profile type foundry located in Marseille, France.  It is best known for the work of the typeface designer Roger Excoffon.  In 1978 the foundry was acquired by the Mergenthaler Linotype Company which transferred photocomposition rights for all faces to Haas.\n\nTelevisa San Ángel: Televisa San Ángel (originally Estudios y Laboratorios San Ángel, S.A.) is a film and television studio located in Mexico City.  It was originally built by Jorge Stahl as a motion picture studio, and in the 1970s would be sold to the Azcárraga family, which, through ownership of the Televisa networks, continues to own the studios.  It is the headquarters facility of the Centro de Educación Artística (CEA) and the Videocine (formerly Televicine) motion picture production and distribution company.  The network's Centro de Post Produccion is also housed at San Ángel.  Moreover, it is best known as a motion picture and television studio.  It is the oldest movie and television production facility in Mexico and the most famous telenovela studio facility in Latin America.  It was one of the four main Mexican film studios along with Estudios Churubusco, Estudios América, and Estudios Tepeyac.\n\nLawrence Livermore National Laboratory: Lawrence Livermore National Laboratory (LLNL) is an American federal research facility in Livermore, California, United States, founded by the University of California in 1952.  A Federally Funded Research and Development Center (FFRDC), it is primarily funded by the U.S. Department of Energy (DOE) and managed and operated by Lawrence Livermore National Security, LLC (LLNS), a partnership of the University of California, Bechtel, BWX Technologies, AECOM, and Battelle Memorial Institute in affiliation with the Texas A&M University System.  In 2012, the laboratory had the synthetic chemical element livermorium named after it.\n\nQuestion: What type of facility was Roger Batzel best known for as director?  \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"facility_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the facility the person directed.\"\n    },\n    \"facility_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the facility.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person at the facility.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"facility_name\",\n    \"facility_type\",\n    \"role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "facility_name": {
        "type": "string",
        "description": "The name of the facility the person directed."
      },
      "facility_type": {
        "type": "string",
        "description": "The type of the facility."
      },
      "role": {
        "type": "string",
        "description": "The role of the person at the facility."
      }
    },
    "required": [
      "person_name",
      "facility_name",
      "facility_type",
      "role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

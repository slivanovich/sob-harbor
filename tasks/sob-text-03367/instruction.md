{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nValentina Kozlova: Valentina Kozlova (born August 26, 1957) is a Soviet-born Russian American ballerina and founder of Valentina Kozlova International Ballet Competition.  In 1979, while on tour as a young principal dancer with the Bolshoi Ballet, Kozlova defected to the United States, where she became a principal dancer with New York City Ballet and later, opened her own ballet school.  Perhaps best known as a lyrical and expressive ballerina, Kozlova is also renowned as a private coach, producing students who have gone on to garner prestigious prizes and positions in companies such as Boston Ballet, American Ballet Theatre Washington Ballet, Stuttgarter Ballet, Les Ballets Trocadéro de Monte Carlo, Universal Ballet, and the National Ballet of Cuba.\n\nPatrick Bissell: Walter Patrick Bissell (December 1, 1957 – December 29, 1987) was an American danseur.  He was a leading principal dancer with the American Ballet Theatre.  On his death at age 30 from a drug overdose, he was described by the artistic director of the American Ballet Theatre Mikhail Baryshnikov as \"without a doubt one of the brightest lights in American Ballet Theater's history, or, for that matter, in the entire ballet world\".  Bissell was noted for his height and athleticism.  His most famous rôle was as Solor in \"La Bayadère\".  His death prompted investigations into the alleged widespread drug use within the American Ballet Theatre.\n\nMagali Messac: Magali Messac, a European/American ballet dancer, was born and raised in the south of France, where she received her early training from Olga and Henry Taneeff.  In 1969, the age of seventeen, she joined the Hamburg Ballet, and four years later, was promoted to principal dancer.  That year, she received the Oberdorfer Culture Award for the most talented young artist.  In 1978, she came to the United States as a principal dancer for the Pennsylvania Ballet, and in 1980, was invited by Mikhail Baryshnikov to join American Ballet Theatre as one of their principal ballerinas.  Ms. Messac finished her performing career in Seattle with the Pacific Northwest Ballet.\n\nCynthia Harvey: Cynthia Harvey (born May 17, 1957) is an American dance teacher and former ballet dancer.  She was a principal dancer for the American Ballet Theatre.  Harvey was born in California, and joined American Ballet Theatre in 1974.  Her roles included Odette/Odile in \"Swan Lake\".  While Mikhail Baryshnikov was the artistic director at ABT, she performed as the prima ballerina in Baryshnikov's filmed production of \"Don Quixote\".\n\nHee Seo: Hee Seo (; born 13 March 1986) is a South Korean principal dancer for American Ballet Theatre (ABT), one of the three leading classical ballet companies in the United States.  She became the company's first Korean ballerina to be promoted to principal dancer in ABT's 75-year history and is one of only three principal dancers in the company who have worked their way up the ranks from the American Ballet Theatre Studio Company.  She is also one of the youngest dancers in ABT history to be promoted to principal at the age of twenty-six. \" The New York Times\" has described her style and dancing to \"exude an unhurried purity that sums up all that is lovely about ballet\" and by \"Vogue\" as \"unspeakably lissome\".  Several critics have noted her style as \"lyrical and open\" and she has been critically acclaimed for her \"humility\" and \"unique feminine strength\".\n\nMichele Wiles: Michele Wiles is an American ballet dancer.  She was a principal dancer with American Ballet Theatre from 2005 - 2011.  In 2011, she left ABT to form the independent classical ballet company Ballet Next with former New York City Ballet principal dancer Charles Askegard.\n\nFrancesca Harper: Francesca Harper (born 1969) is an American dancer and choreographer.  She is the daughter of dancer and educator Denise Jefferson and niece of Pulitzer Prize winning writer Margo Jefferson.  Harper was named a scholar of the arts in the Presidential Scholars Program in 1987.  She studied at the School of American Ballet and the Joffrey Ballet School and went on to become the principal dancer in William Forsythe’s Ballet Frankfurt from 1994-1999.  She was a ballet consultant for the film Black Swan, and has appeared as a dancer in the television series Boardwalk Empire.  In 2005, she founded the non-profit dance company The Francesca Harper Project.  Long Island University honored her with a \"Living History\" award during Black History Month in 2013.\n\nBlack Swan dance double controversy: \"Black Swan\" is a 2010 American psychological thriller film about a ballet dancer directed by Darren Aronofsky and starring Natalie Portman, Vincent Cassel, and Mila Kunis.  After the 83rd Academy Awards, in which Portman won the Oscar for Best Actress for her role in the film as a ballerina, controversy arose over how much credit for the dancing in the film was being given to her and how much to her \"dance double\", American Ballet Theatre soloist Sarah Lane.\n\nSarah Lane: Sarah Lane (born August 3, 1983/1984) is an American ballet dancer and a principal dancer with American Ballet Theatre (ABT).\n\nRoberto Bolle: Roberto Bolle (Casale Monferrato, March 26, 1975) is an Italian danseur.  He is currently a \"principal dancer\" with the American Ballet Theatre and a principal dancer \"étoile\" at La Scala Theatre Ballet.  Bolle also dances regularly as a guest artist with the world’s leading companies, including The Royal Ballet, the Mariinsky Ballet, the Bolshoi Ballet and the Paris Opera Ballet.\n\nQuestion: The dance double in the Black Swan dance double controversy involved which principal dancer of the American Ballet Theatre?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"controversy_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the controversy.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film central to the controversy.\"\n    },\n    \"dance_double_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"dancer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the dancer who served as the dance double.\"\n        },\n        \"ballet_company\": {\n          \"type\": \"string\",\n          \"description\": \"The ballet company the dance double is associated with.\"\n        },\n        \"dancer_rank\": {\n          \"type\": \"string\",\n          \"description\": \"The rank of the dancer within their ballet company.\"\n        }\n      },\n      \"required\": [\n        \"dancer_name\",\n        \"ballet_company\",\n        \"dancer_rank\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"controversy_name\",\n    \"film_title\",\n    \"dance_double_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "controversy_name": {
        "type": "string",
        "description": "The name of the controversy."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film central to the controversy."
      },
      "dance_double_details": {
        "type": "object",
        "properties": {
          "dancer_name": {
            "type": "string",
            "description": "The name of the dancer who served as the dance double."
          },
          "ballet_company": {
            "type": "string",
            "description": "The ballet company the dance double is associated with."
          },
          "dancer_rank": {
            "type": "string",
            "description": "The rank of the dancer within their ballet company."
          }
        },
        "required": [
          "dancer_name",
          "ballet_company",
          "dancer_rank"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "controversy_name",
      "film_title",
      "dance_double_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

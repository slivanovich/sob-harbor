{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTrevor Rhone: Trevor Dave Rhone (24 March 1940 – 15 September 2009) was a Jamaican writer, playwright and film maker.  He co-wrote, with director Perry Henzell, the internationally successful film \"The Harder They Come\" (1972).\n\nLGBT ageing: LGBT ageing addresses issues and concerns related to ageing and minority sexualities or gender identities.  Older LGBT* people are marginalised by: a) younger LGBT people, because of ageism and age discrimination; and b) by older age social networks because of heteronormativity (the assumption that heterosexuality is the norm), heterosexism (the privileging of heterosexuality), biphobia, homophobia and transphobia (prejudice and discrimination towards LGBT people).\n\nCinema of Jamaica: Despite Jamaica never having a very strong film industry, the island has produced notable films from the 1970s onwards.  The most critically acclaimed film is \"The Harder They Come\", by Perry Henzell which received international acclaim.  The Jamaican government and various private citizens have tried to promote the creation of new films by the creation of certain agencies such as the Jamaican Film Commission, and film festivals such as the Reggae Film Festival.  \"The Harder They Come\" sparked trends that were apparent in following films such as \"Dancehall Queen\" and \"One Love\", both directed by Don Letts and Rick Elgood.\n\nThe Harder They Come: The Harder They Come is a 1972 Jamaican crime film directed by Perry Henzell and co-written by Trevor D. Rhone, and starring Jimmy Cliff.  The film is most famous for its reggae soundtrack that is said to have \"brought reggae to the world\".\n\nSuccessful aging: Successful aging (American English) or successful ageing (British English) refers to physical, mental and social well-being in older age.  The concept of successful aging can be traced back to the 1950s, and was popularized in the 1980s.  It reflects changing view on aging in Western countries, where a stigma associated with old age (see ageism) has led to considering older people as a burden on society.  Consequently, in the past most of the scientists have been focusing on negative aspects of aging or preventing the decline of youth.\n\nAlbert Ray: Albert Ray (August 28, 1897 – February 5, 1944) was an American film director, actor and screenwriter.  He directed 76 films between 1920 and 1939.  He also appeared in 18 films between 1915 and 1922.  He was born in New Rochelle, New York and died in Los Angeles, California.\n\nChild sex ratio: In India, the Child Sex Ratio is defined as the number of females per thousand males in the age group 0–6 years in a human population.  Thus it is equal to 1000 x the reciprocal of the sex ratio (ratio of males to females in a population) in the same age group, i.e. under age seven.  Obviously, an imbalance in this age group will extend to older age groups in future years.  Currently, the ratio of males to females is generally significantly greater than 1, i.e. there are more boys than girls.\n\nSexuality in older age: Sexuality in older age concerns the sexual drive, sexual activity and overall sexuality of people in middle age and those in old age, and the social perceptions about sexuality in older age.  Older people engage in a variety of sexual acts from time to time for a variety of reasons.  While the human body has some limits on the maximum age for reproduction, sexual activity can be performed or experienced well into the later years of life.  Sexuality in older age is often considered a taboo, and this can affect how older individuals experience their sexuality.\n\nLove, Sex, and Aging: Love, Sex, and Aging is a 1984 book on sexuality in older age by medical writer Edward M. Brecher and the editors of Consumer Reports.  The book presents survey research describing the attitudes and experiences of older people in the United States based on a 1977 Consumer Reports survey of over 4000 people.  One reason for the study was to demonstrate that older people can have healthy sex lives.  At the time and place of publication, this topic was not commonly discussed.\n\nPerry Henzell: Perry Henzell (7 March 1936 – 30 November 2006) was most famous for being the director of the first Jamaican feature film, \"The Harder They Come\" (1972) co-written by Trevor D. Rhone, starring Jimmy Cliff.\n\nQuestion: Which director lived to an older age, Albert Ray or Perry Henzell?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"older_director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director who lived to an older age.\"\n    },\n    \"directors_compared\": {\n      \"type\": \"array\",\n      \"description\": \"Details for each director involved in the comparison.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the director.\"\n          },\n          \"birth_date\": {\n            \"type\": \"string\",\n            \"format\": \"date\",\n            \"description\": \"The birth date of the director (YYYY-MM-DD).\"\n          },\n          \"death_date\": {\n            \"type\": \"string\",\n            \"format\": \"date\",\n            \"description\": \"The death date of the director (YYYY-MM-DD).\"\n          },\n          \"age_at_death_years\": {\n            \"type\": \"integer\",\n            \"description\": \"The age of the director at the time of death in full years.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"birth_date\",\n          \"death_date\",\n          \"age_at_death_years\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"age_difference_years\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in age at death between the two directors in years.\"\n    }\n  },\n  \"required\": [\n    \"older_director_name\",\n    \"directors_compared\",\n    \"age_difference_years\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "older_director_name": {
        "type": "string",
        "description": "The name of the director who lived to an older age."
      },
      "directors_compared": {
        "type": "array",
        "description": "Details for each director involved in the comparison.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the director."
            },
            "birth_date": {
              "type": "string",
              "format": "date",
              "description": "The birth date of the director (YYYY-MM-DD)."
            },
            "death_date": {
              "type": "string",
              "format": "date",
              "description": "The death date of the director (YYYY-MM-DD)."
            },
            "age_at_death_years": {
              "type": "integer",
              "description": "The age of the director at the time of death in full years."
            }
          },
          "required": [
            "name",
            "birth_date",
            "death_date",
            "age_at_death_years"
          ],
          "additionalProperties": false
        }
      },
      "age_difference_years": {
        "type": "integer",
        "description": "The difference in age at death between the two directors in years."
      }
    },
    "required": [
      "older_director_name",
      "directors_compared",
      "age_difference_years"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

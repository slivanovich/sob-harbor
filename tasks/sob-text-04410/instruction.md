{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSling Blade (film): Sling Blade is a 1996 American drama film set in rural Arkansas, written and directed by Billy Bob Thornton, who also stars in the lead role.  It tells the story of a man named Karl Childers who has a developmental disability and is released from a psychiatric hospital, where he has lived since killing his mother and her lover when he was 12 years old, and the friendship he develops with a young boy and his mother.  In addition to Thornton, it stars Dwight Yoakam, J. T. Walsh, John Ritter, Lucas Black, Natalie Canerday, James Hampton, and Robert Duvall.\n\nBilly Bob Thornton: William Robert \"Billy Bob\" Thornton (born August 4, 1955) is an American actor, filmmaker, singer, songwriter, and musician.\n\nOne False Move: One False Move is a 1992 American thriller film co-written by Billy Bob Thornton.  The film stars Thornton alongside Bill Paxton and Cynda Williams and was directed by Carl Franklin.  The low-budget production was about to be released straight to home video when it was finished, but became popular through word of mouth, convincing the distributor to give the film a theatrical release.  Film critic Gene Siskel voted this film as his favorite of 1992.\n\nJayne Mansfield's Car: Jayne Mansfield's Car is a 2012 drama film directed by Billy Bob Thornton, marking his first directing job since 2001's \"Daddy and Them\".  Thornton also stars alongside Robert Duvall, John Hurt, Kevin Bacon, Ray Stevenson, Frances O'Connor, Ron White, and Robert Patrick. <ref name=\"http://www.deadline.com/2011/06/billy-bob-thornton-sets-cast-funding-for-first-directing-effort-in-decade/\"> </ref> The film had its world premiere at the 62nd Berlin International Film Festival in February 2012.  The film was released in limited release on September 13, 2013.\n\nThe Gift (2000 film): The Gift is a 2000 American supernatural thriller film directed by Sam Raimi, written by Billy Bob Thornton and Tom Epperson and based on the alleged psychic experiences of Thornton's mother.\n\nBandits (2001 film): Bandits is a 2001 American criminal comedy-drama film directed by Barry Levinson.  It stars Bruce Willis, Billy Bob Thornton, and Cate Blanchett.  Filming began in October 2000 and ended in February 2001.  It helped Thornton earn a National Board of Review Best Actor Award for 2001.  Thornton and Blanchett's performances earned praise, as each was nominated for Best Actor and Best Actress Golden Globe Awards for their performances in this film, while Blanchett was nominated for Best Supporting Actress at the Screen Actors Guild Awards.  It first opened in theaters on October 12, 2001.\n\nDaddy and Them: Daddy and Them is a 2001 American film written, directed by, and starring Billy Bob Thornton.  In addition to Thornton, it stars Laura Dern, Andy Griffith, Ben Affleck, Kelly Preston, Diane Ladd, Brenda Blethyn, Tuesday Knight, Jamie Lee Curtis and Jim Varney.  This was Jim Varney's last live-action film; he died a year before the movie's release.  It was also his penultimate movie.\n\nGene Saks: Gene Saks (November 8, 1921 – March 28, 2015) was an American stage, film director, and actor.  An inductee of the American Theater Hall of Fame, his acting career beginning with a debut on Broadway in 1949.  As a director, he was nominated for seven Tony Awards, winning three for his direction of \"I Love My Wife\", \"Brighton Beach Memoirs\" and \"Biloxi Blues\".  He also directed a number of films during his career.  He was married to Bea Arthur, who died in 2009, from 1950 until 1980, and subsequently to Keren Saks, from 1980 to his death in 2015.\n\nChrystal (film): Chrystal is an American drama film, which was released to audiences in the United States on April 8, 2005.  The cast included Billy Bob Thornton, Lisa Blount, Harry Lennix, Walton Goggins, and Grace Zabriskie.  Ray McKinnon, in addition to playing the role of \"Snake\", directed, wrote, and produced the film.  The story is about a woman named Chrystal (Lisa Blount) who has been traumatized both physically and mentally from a car accident that took the life of her son.  Joe (Billy Bob Thornton), Chrystal's husband, has just been released from jail after a 16-year sentence stemming from multiple crimes he committed.\n\nA Simple Plan (film): A Simple Plan is a 1998 American neo-noir crime thriller film adapted by Scott B. Smith from his 1993 novel of the same name.  Directed by Sam Raimi, it stars Bill Paxton, Billy Bob Thornton and Bridget Fonda.  Set in rural Minnesota, \"A Simple Plan\" follows brothers Hank (Paxton) and Jacob Mitchell (Thornton), who, along with Jacob's friend Lou (Brent Briscoe), discover a crashed plane containing $4.4 million in cash.  The three men go to great lengths to keep the money a secret but begin to doubt each other's trust, resulting in lies, deceit and murder.\n\nQuestion: Billy Bob Thornton and Gene Saks, are Americans that have which occupation in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person mentioned.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person mentioned.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality shared by both individuals.\"\n    },\n    \"shared_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation that both individuals have in common.\"\n    },\n    \"person_1_other_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other occupations of the first person, if any.\"\n    },\n    \"person_2_other_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other occupations of the second person, if any.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_2_name\",\n    \"nationality\",\n    \"shared_occupation\",\n    \"person_1_other_occupations\",\n    \"person_2_other_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person mentioned."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person mentioned."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality shared by both individuals."
      },
      "shared_occupation": {
        "type": "string",
        "description": "The occupation that both individuals have in common."
      },
      "person_1_other_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other occupations of the first person, if any."
      },
      "person_2_other_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other occupations of the second person, if any."
      }
    },
    "required": [
      "person_1_name",
      "person_2_name",
      "nationality",
      "shared_occupation",
      "person_1_other_occupations",
      "person_2_other_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

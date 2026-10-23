{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMartin W. Littleton: Martin Wiley Littleton (January 12, 1872 – December 19, 1934) was an American attorney known for his involvement in a number of high-profile trials during the early 1900s, including serving as chief defense counsel for Harry Kendall Thaw at his second trial in 1908 for the murder of renowned architect Stanford White, and defending Harry Ford Sinclair, the head of Sinclair Oil, from criminal charges resulting from the Teapot Dome scandal.  Littleton also served one term as United States Representative from New York from 1911 to 1913, and was borough president of Brooklyn.\n\nDharhara, Bhagalpur: Dharhara is a village in the Bhagalpur District of Bihar, India.  there is a tradition of plantation when girl born in any family of this village.  this tradition help to save trees and girl both.\n\nAlice Delysia: Alice Henriette Lapize (3 March 1889 – 10 February 1979), better known by her stage name, Alice Delysia and sometimes Elise Delisia, was a French actress and singer who made her career in English musical theatre.  After performing in the chorus at the Moulin Rouge and other theatres in Paris from the age of 14, she became a chorus girl in Edwardian musical comedies, briefly on Broadway in 1905, then in London for several years and back in Paris in 1912.\n\nChorus Equity Association: The Chorus Equity Association was created on August 12, 1919, in New York City during the strike by the Actors' Equity Association.  After Florenz Ziegfeld revealed that he was joining the Producing Managers' Association, the chorus girls in his Ziegfeld Follies created their own union, with the help of a substantial donation from the superstar actress and former chorus girl Lillian Russell.\n\nEvelyn Nesbit: Florence Evelyn Nesbit (December 25, 1884 – January 17, 1967), known professionally as Evelyn Nesbit, was a popular American chorus girl, an artists' model, and an actress.\n\nWilliam Lewis Shurtleff: William Lewis Shurtleff, K.C., LL.D. , (March 29, 1864 – January 1, 1954) was a Quebec lawyer and newspaper owner.  He was the defense lawyer for Harry Kendall Thaw in 1913.  The \"Buffalo Morning Express\" calls him \"one of the leading lawyers in Canada\".\n\nThe Unwritten Law (1907 film): The Unwritten Law: A Thrilling Drama Based on the Thaw-White Case is a 1907 film produced by the Lubin Manufacturing Company, based on the true crime story of Harry Kendall Thaw's murder of Stanford White over his involvement with model and actress Evelyn Nesbit.  Produced and released concurrently with Thaw's trial, its depiction of a recent sexual scandal led to widespread controversy, becoming \"the first film in the United States to be widely construed as 'scandalous.'\"\n\nDetroit Regional Yacht-racing Association: The Detroit Regional Yacht-racing Association (DRYA) was established in 1912 as the Detroit River Yachting Association by the Commodores of the Detroit Boat Club and the Detroit Yacht Club, Commodore Harry Austin and Commodore Harry Kendall, respectively.\n\nChorus Girl (album): Chorus Girl was the first \"chorus\" compilation album made and released by Atomic Records.  The album contains various songs from the 1980s, mainly new wave.  It was succeeded by a second album, entitled \"Chorus 2\".\n\nHarry Kendall Thaw: Harry Kendall Thaw (February 12, 1871 – February 22, 1947) was the son of Pittsburgh coal and railroad baron William Thaw, Sr. Heir to a multimillion-dollar mine and railroad fortune, Thaw had a history of severe mental instability and led a profligate life.  His historical legacy rests on one notorious act: on June 25, 1906, on the rooftop of Madison Square Garden, Thaw murdered renowned architect Stanford White, who was having an affair with Thaw's wife, model/chorus girl Evelyn Nesbit.\n\nQuestion: Harry Kendall Thaw's wife was a chorus girl born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was Harry Kendall Thaw's wife.\"\n    },\n    \"relationship_to_thaw\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the person to Harry Kendall Thaw.\"\n    },\n    \"profession\": {\n      \"type\": \"string\",\n      \"description\": \"One of the professions of the person.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"relationship_to_thaw\",\n    \"profession\",\n    \"birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who was Harry Kendall Thaw's wife."
      },
      "relationship_to_thaw": {
        "type": "string",
        "description": "The relationship of the person to Harry Kendall Thaw."
      },
      "profession": {
        "type": "string",
        "description": "One of the professions of the person."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the person."
      }
    },
    "required": [
      "person_name",
      "relationship_to_thaw",
      "profession",
      "birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

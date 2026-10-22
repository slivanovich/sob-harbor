Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Joint Security Area (film): Joint Security Area (Korean: 공동경비구역 JSA ) is a 2000 South Korean mystery thriller film starring Lee Young-ae, Lee Byung-hun and Song Kang-ho.  It was directed by Park Chan-wook and is based on the novel "DMZ" by Park Sang-yeon.  The film, which was shot on location in South Korea, concerns an investigation into the circumstances surrounding a fatal shooting incident within the DMZ, the heavily fortified border that separates North and South Korea.

Mr. Sunshine (2018 TV series): Mr. Sunshine () is an upcoming South Korean television series written by Kim Eun-sook and directed by Lee Eung-bok, starring Lee Byung-hun, Kim Tae-ri and Yoo Yeon-seok.  The series will air on cable network tvN in early 2018.

Inside Men (film): Inside Men () is a 2015 South Korean neo noir political crime action film written and directed by Woo Min-ho based on Yoon Tae-ho's webtoon "The Insiders" that dissects the corruption within Korean society.  Starring Lee Byung-hun, Jo Seung-woo and Baek Yoon-sik, it began filming in July 2014 and was released in theaters on November 19, 2015.

A Bittersweet Life: A Bittersweet Life (; lit.  "The Sweet Life") is a 2005 South Korean gangster action drama film written and directed by Kim Jee-woon and starring Lee Byung-hun.

Lee Byung-hun: Lee Byung-hun (Korean: 이병헌 ; born July 12, 1970) is a South Korean actor, singer and model.  He has received critical acclaim for his work in a wide range of genres, most notably "Joint Security Area" (2000); "A Bittersweet Life" (2005); "The Good, the Bad, the Weird" (2008); the television series "Iris" (2009); "I Saw the Devil" (2010); and "Masquerade" (2012).  His critically acclaimed film "Inside Men" (2015) won him the Best Actor prize in three prestigious award ceremonies: 52nd Baeksang Art Awards, 37th Blue Dragon Awards and 53rd Grand Bell Awards—a feat that was unbroken since 2004.  Lee has five films—"Joint Security Area", "The Good, the Bad, the Weird", "Masquerade", "Inside Men" and "Master"—on the list of highest-grossing films in South Korea.

The Magnificent Seven (2016 film): The Magnificent Seven is a 2016 American Western action film directed by Antoine Fuqua and written by Nic Pizzolatto and Richard Wenk.  It is a remake of the 1960 western film of the same name, which in turn was a reimagination of Akira Kurosawa's 1954 Japanese film "Seven Samurai".  The film stars Denzel Washington, Chris Pratt, Ethan Hawke, Vincent D'Onofrio, Lee Byung-hun, Manuel Garcia-Rulfo, Martin Sensmeier, Haley Bennett, and Peter Sarsgaard.  It is the final film of composer James Horner, who died the previous year after composing a part of the score; his friend Simon Franglen completed the music.

I Saw the Devil: I Saw the Devil () is a 2010 South Korean psychological action thriller film directed by Kim Jee-woon, written by Park Hoon-jung, and starring Lee Byung-hun and Choi Min-sik.  The film introduces the character of NIS agent Kim Soo-hyun (Lee Byung-hun), who embarks on a quest of revenge when his fiancée is brutally murdered by a psychopathic murderer, Jang Kyung-chul (Choi Min-sik).  The line between good and evil begins to blur when the two play a dangerous game of cat and mouse.  "I Saw the Devil" made its premiere in the United States at the 2011 Sundance Film Festival and had a limited U.S theatrical release.

Pudhupettai: Pudhupettai (Tamil: புதுப்பேட்டை English: New Hood/Area) is a 2006 Indian Tamil neo noir gangster film written and directed by Selvaraghavan, starring his brother Dhanush in the lead, whilst Sneha and Sonia Agarwal enact the lead female character roles.  The film, with music scored by Yuvan Shankar Raja and cinematography by Arvind Krishna, Selvaraghavan's usual crew members, released on 26 May 2006, receiving universal critical acclaim for the music which gives a huge hype to the movie and picturisation.  The film is characterized as a modern cult gangster.  The film was dubbed into Telugu and released as "Dhoolpeta".

Gangsters Versus Cowboys: Gangsters Versus Cowboys (Spanish:Gangsters contra charros) is a 1948 Mexican gangster film written, directed by, and starring Juan Orol, and featuring Rosa Carmina and José Pulído.  It was made as a sequel to Orol's "Gangster's Kingdom".  However, it has become a cult film due to its low-budget production values and idiosyncratic style.

Addicted (2002 film): Addicted is a 2002 South Korean thriller film directed by Park Young-hoon and starring Lee Byung-hun and Lee Mi-yeon.  In 2009 it was remade into an American film called "Possession".

Question: Lee Byung-hun worked on the 2005 gangster film written and directed by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the film."
    },
    "director_writer": {
      "type": "string",
      "description": "The name of the person who wrote and directed the film."
    },
    "starring_actor": {
      "type": "string",
      "description": "The name of the actor who starred in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "director_writer",
    "starring_actor"
  ],
  "additionalProperties": false
}

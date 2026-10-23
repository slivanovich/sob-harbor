{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWet Seal: Wet Seal was an American teen clothing retailer headquartered in Foothill Ranch, California.  It carried low, budget or economy priced brand name and company-designed apparel and accessories.  The company was founded in Newport Beach, California by Lorne Huycke in 1962 as \"Lorne's.\"  The \"Wet Seal\" name comes from a comment Lorne Huycke made during a fashion show commenting that a model wearing a bathing suit looked like a \"wet seal.\"  The company was incorporated as Wet Seal in 1990.\n\nThe Princess and the Marine: The Princess and the Marine is a 2001 American made for television movie based on the true story of American Marine Jason Johnson and Bahrain Princess Meriam Al-Khalifa, with stars Mark-Paul Gosselaar and Marisol Nichols in the roles of Jason and Meriam.\n\nBarry Seal: Adler Berriman \"Barry\" Seal (July 16, 1939 – February 19, 1986) was an American airline pilot who became a major drug smuggler for the Medellín Cartel.  When Seal was convicted of smuggling charges, he became an informant for the Drug Enforcement Administration and testified in several major drug trials.  He was murdered in 1986 by contract killers hired by Pablo Escobar, head of the Medellín Cartel.\n\nAmerican Made (song): \"American Made\" is a song written by Bob DiPiero and Pat McManus, and recorded by American country music group The Oak Ridge Boys.  It was released in February 1983 as the first single and title track from the album \"American Made\".  The song was The Oak Ridge Boys' seventh number one on the country chart.  The single went to number one for one week and spent a total of thirteen weeks on the country chart.  \"American Made was also one of their biggest cross-over hits peaking at number seventy-two on the Hot 100.\n\nAmerican Made (The Oak Ridge Boys album): American Made is the eighth country studio album by The Oak Ridge Boys, released in 1983.  It featured yet another \"crossover hit\" with the song \"American Made\", which hit #1 on the country charts (on April 23, 1983) and #72 on the U.S. Hot 100 singles chart.\n\nAmerican Made (film): American Made is a 2017 American biographical crime film directed by Doug Liman, written by Gary Spinelli and starring Tom Cruise, Domhnall Gleeson, Sarah Wright, Alejandro Edda, Mauricio Mejía, Caleb Landry Jones and Jesse Plemons.  The plot focuses on Barry Seal, a former TWA pilot who became a drug smuggler for the Medellín Cartel in the 1980s.  In order to avoid jail time, Seal approached United States government officials and served as an informant for the DEA.\n\nAmerican Made Music to Strip By: American Made Music to Strip By is the first remix album released by American musician Rob Zombie.  The album was released through Geffen Records on October 26, 1999.  It is composed entirely of remixes of songs taken from Zombie's debut studio album, \"Hellbilly Deluxe\" (1998).  Zombie worked with a number of musicians and producers to create updated versions of the songs, including Charlie Clouser, who had previously worked with Zombie on his debut solo effort.  Ten of the original albums songs have been remixed, excluding three instrumental interludes.  Two of the remixes featured on \"American Made Music to Strip By\" had previously been released on promotional discs for \"Dragula\" (1998) and \"Living Dead Girl\" (1999).\n\nBarry Seal (politician): Barry Seal (born 28 October 1937) is a British Labour Party politician.  He was Member of the European Parliament (MEP) for the single-member seat of Yorkshire West from 1979 to 1999.  He stood unsuccessfully for election to the new multi-member seat of Yorkshire and the Humber in the 1999 European elections.  Seal also stood for selection as Labour candidate for the Bradford North constituency in the 1987 election, receiving 12 votes and coming second to Pat Wall who went on to win the election for Labour.\n\nBuild with America: Build With America is a national radio program and campaign.  This program features American made home construction and home improvement products.  The expressed intention of this program is to inform the consumer of American made home construction and home improvement products, and to increase the consumer's purchases of these products.  The creation of this program was inspired by the Bozeman, Montana home that was built with 100% American made home construction and home improvement products.\n\nAditya Seal: Aditya Seal (born 22 March 1987) is an Indian model and film actor best known for his work in bollywood.  Seal made his début with the movie \"Ek Chhotisi Love Story\", where he played a teenager opposite to Manisha Koirala.  Seal was a world Taekwondo champion.  His Co-stars in Purani Jeans wereTanuj Virwani And Izabelle Leite.  In 2016, he played the role of Shekhar in Tum Bin II and received praise for his versatility as an actor.\n\nQuestion: What cartel did Barry Seal work for in the movie \"American Made?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character in the film.\"\n    },\n    \"cartel_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cartel the character worked for.\"\n    },\n    \"character_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the character in relation to the cartel.\"\n    },\n    \"movie_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"character_name\",\n    \"cartel_name\",\n    \"character_role\",\n    \"movie_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character in the film."
      },
      "cartel_name": {
        "type": "string",
        "description": "The name of the cartel the character worked for."
      },
      "character_role": {
        "type": "string",
        "description": "The role of the character in relation to the cartel."
      },
      "movie_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "movie_title",
      "character_name",
      "cartel_name",
      "character_role",
      "movie_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

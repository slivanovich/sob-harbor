{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nQ-Tip (musician): Kamaal Ibn John Fareed (born Jonathan William Davis; April 10, 1970), better known by his stage name Q-Tip, is an American rapper, singer, actor, record producer and DJ.  He embarked on his music career as part of the critically acclaimed East Coast hip hop group A Tribe Called Quest.  John Bush of AllMusic called him \"the best rapper/producer in hip-hop history,\" while editors of About.com placed him #17 on their list of the Top 25 Hip-Hop Producers, as well as placing him #38 on their list of the Top 50 MCs of Our Time.  In 2012, \"The Source\" ranked him #20 on their list of the Top 50 Lyricists of All Time.\n\nScarface (rapper): Brad Terrence Jordan (born November 9, 1970), better known by his stage name Scarface, is an American rapper and music producer.  He hails from Houston, Texas and is a former member of the Geto Boys.  He is originally from the city's South Acres (Crestmont Park) neighborhood.  In 2012, \"The Source\" ranked him #16 on their list of the Top 50 Lyricists of All Time, while About.com ranked him #10 on its list of the 50 Greatest MCs of Our Time (1987-2007).\n\nThere's a God on the Mic: There’s a God on the Mic: The True 50 Greatest MCs is a 2003 book by the old school hip hop MC Kool Moe Dee, where he ranks what he believes to be the Top 50 greatest MCs of all time, giving a breakdown of each artist.  The book also features a foreword from Chuck D and includes full color photos from hip hop photographer Ernie Paniccioli.\n\nSlick Rick: Richard Martin Lloyd Walters (born January 14, 1965; better known as Slick Rick, Rick The Ruler and MC Ricky D) is a British-born American rapper.  He has released four albums: \"The Great Adventures of Slick Rick\" (1988), \"The Ruler's Back\" (1991), \"Behind Bars\" (1994) and \"The Art of Storytelling\" (1999).  His music has been sampled and interpolated over 600 times, in over 35 songs by artists including Beyoncé, The Beastie Boys, TLC, Nas, Miley Cyrus, Kanye West, Black Star, The Notorious B.I.G., Snoop Dogg, MC Ren, and Color Me Badd.  In the process, Walters has become the most-sampled hip-hop artist ever.  Many of the new songs became hit singles.  He's been a VH-1 \"Hip Hop Honors\" honoree, and About.com ranked him  12 on their list of the Top 50 MCs of Our Time, while \"The Source\" ranked him No. 15 on their list of the Top 50 Lyricists of All Time.  He has acted and cameoed in 10 movies and videos.\n\nChuck D: Carlton Douglas Ridenhour (born August 1, 1960), known professionally as Chuck D, is an American rapper, author, and producer.  As the leader of the rap group Public Enemy, he helped create politically and socially conscious hip hop music in the mid-1980s.  About.com ranked him at No. 9 on their list of the Top 50 MCs of All Time, while \"The Source\" ranked him at No. 12 on their list of the Top 50 Hip-Hop Lyricists of All Time.\n\nPrince Ea: Richard Williams, better known by his stage name Prince Ea, is an American spoken word artist, poet, rapper and filmmaker.  After graduating from the University of Missouri–St. Louis with a degree in anthropology, he initially pursued a career as a hip hop artist.  Inspired by artists like Immortal Technique and Canibus, he started and popularized the \"Make S.M.A.R.T Cool\" movement to promote values like intelligence, free thought, unity, and creativity in hip hop music and culture.\n\nRas Kass: John Austin IV (born September 26, 1973), better known by his stage name Ras Kass, is an American rapper.  He returned as a member of the hip hop supergroup The HRSMN along with Canibus, Killah Priest, and Kurupt in 2014.  Ras is a member of the group Golden State Warriors with Xzibit and Saafir.  Editors of About.com ranked him #30 on their list of the \"Top 50 MCs of Our Time (1987–2007)\".  Pitchfork Media called him \"one of the best rappers of all time.\"\n\nCanibus: Germaine Williams (born December 9, 1974), better known by his stage name Canibus, is an American rapper and actor.  He is a member of The HRSMN, Sharpshooterz, Cloak N Dagga, The Undergods, and one-half of T.H.E.M. Canibus rose to fame in the mid-nineties.  About.com placed him at number 32 on their list of the \"Top 50 MCs of Our Time (1987–2007)\", while in 2012 \"The Source\" placed him number 44 on their list of the Top 50 Lyricists of All Time.\n\nAZ (rapper): Anthony Cruz (born March 9, 1972), better known by his stage name AZ, is an American rapper born in Brooklyn, NY.  He is known for being a longtime and frequent rhyme partner of Nas, and also a member of hip-hop group The Firm alongside Nas, Foxy Brown, Cormega and Nature.  In a countdown of the 10 Most Underappreciated Rappers—Most Underrated Rappers of All Time, the editors of About.com listed AZ as #1 on the list.  He was also included on About.com's list of the Top 50 MCs of Our Time (1987–2007), where he was described as \"arguably the most underrated lyricist ever. \"AZ first became known by appearing on Nas' landmark 1994 album \"Illmatic\" on the song \"Life's a Bitch\", as well as featuring vocals on the opening track The Genesis.  AZ signed with EMI, and soon released his debut album \"Doe Or Die\" in 1995 to critical acclaim.  The album's lead single, \"Sugar Hill\", became AZ's major commercial success as a solo artist, reaching #25 on the \"Billboard\" Hot 100 chart, and achieving Gold status.  AZ's EMI contract was transferred to sister label Noo Trybe/Virgin Records when the EMI Label Group was shut down.\n\nRoyce da 5'9&quot;: Ryan Daniel Montgomery (born July 5, 1977), better known by his stage name Royce da 5′9″, is an American rapper from Detroit, Michigan.  He is best known for his longtime association with Eminem as well as his solo career, recording primarily with producers Carlos \"6 July\" Broady and DJ Premier, as well as ghostwriting for the likes of Diddy and Dr. Dre.  Royce is one half of the rap duo Bad Meets Evil with Eminem, one quarter of the hip hop group Slaughterhouse with Joe Budden, Joell Ortiz and Crooked I, and one half of the hip hop group PRhyme with DJ Premier.  The editors of About.com ranked him No. 30 on their list of the Top 50 MCs of Our Time (1987–2007).\n\nQuestion: Which artist inspired Prince Ea and was placed at number 32 on the list of the \"Top 50 MCs of Our Time (1987-2007)?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who meets the criteria.\"\n    },\n    \"inspiration_for\": {\n      \"type\": \"string\",\n      \"description\": \"The artist who was inspired by the identified artist.\"\n    },\n    \"ranking_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"list_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the list on which the artist was ranked.\"\n        },\n        \"rank\": {\n          \"type\": \"integer\",\n          \"description\": \"The rank achieved by the artist on the specified list.\"\n        },\n        \"source\": {\n          \"type\": \"string\",\n          \"description\": \"The publication or entity that created the list.\"\n        }\n      },\n      \"required\": [\n        \"list_name\",\n        \"rank\",\n        \"source\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"inspiration_for\",\n    \"ranking_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who meets the criteria."
      },
      "inspiration_for": {
        "type": "string",
        "description": "The artist who was inspired by the identified artist."
      },
      "ranking_details": {
        "type": "object",
        "properties": {
          "list_name": {
            "type": "string",
            "description": "The name of the list on which the artist was ranked."
          },
          "rank": {
            "type": "integer",
            "description": "The rank achieved by the artist on the specified list."
          },
          "source": {
            "type": "string",
            "description": "The publication or entity that created the list."
          }
        },
        "required": [
          "list_name",
          "rank",
          "source"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "artist_name",
      "inspiration_for",
      "ranking_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

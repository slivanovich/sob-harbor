{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlame Canada: \"Blame Canada\" is a song from the 1999 animated musical fantasy comedy film \"\", written by Trey Parker & Marc Shaiman.  In the song, the parents of the fictional \"South Park\", led by Sheila Broflovski (Mary Kay Bergman), decided to blame Canada for the trouble their children have been getting into since watching the Canadian-made movie \"Terrance and Phillip: Asses of Fire\" and imitating what they saw and heard in the movie.  \"Blame Canada\" satirizes scapegoating and parents that do not control \"their children's consumption of popular culture\".  In the 2014 game \"\", the song was made 8-Bit.\n\nThe Sword in the Stone (film): The Sword in the Stone is a 1963 American animated musical fantasy comedy film produced by Walt Disney and released by Buena Vista Distribution.  The 18th Disney animated feature film, it was the final Disney animated film to be released before Walt Disney's death.  The songs in the film were written and composed by the Sherman Brothers, who later wrote music for other Disney films like \"Mary Poppins\" (1964), \"The Jungle Book\" (1967), \"The Aristocats\" (1970), and \"Bedknobs and Broomsticks\" (1971).\n\nThe Road to El Dorado: The Road to El Dorado is a 2000 American animated adventure musical fantasy comedy film produced by DreamWorks Animation.  It was directed by Eric \"Bibo\" Bergeron and Don Paul; Will Finn and David Silverman directed additional sequences.  The film stars Kevin Kline, Kenneth Branagh, Armand Assante, Jim Cummings, Edward James Olmos, Tobin Bell and Rosie Perez.  The soundtrack features songs by Elton John and Tim Rice, as well as composers Hans Zimmer and John Powell.\n\nYellow Submarine (film): Yellow Submarine (also known as The Beatles: Yellow Submarine) is a 1968 British animated musical fantasy comedy film inspired by the music of the Beatles, directed by animation producer George Dunning, and produced by United Artists and King Features Syndicate.  Initial press reports stated that the Beatles themselves would provide their own character voices; however, aside from composing and performing the songs, the real Beatles participated only in the closing scene of the film, while their cartoon counterparts were voiced by other actors.\n\nThe Pick of Destiny Tour (2006–2007): The 2006–2007 World Tour (better known as The Pick of Destiny Tour) was a worldwide concert tour by American rock band Tenacious D.  The tour was in support of the band's 2006 comedy movie \"Tenacious D in The Pick of Destiny\" and its soundtrack album \"The Pick of Destiny\", and visited North America, the United Kingdom and Australasia.  The tour began on November 11, 2006 and ended on February 21, 2007, featuring 32 shows in total.  Footage from the shows at the Paramount Theatre in Seattle on February 16 and 17, 2007 were released in the form of \"The Complete Master Works 2\" in November 2008.\n\nKazaam: Kazaam is a 1996 American musical fantasy comedy film directed by Paul Michael Glaser, written by Christian Ford and Roger Soffer based on a story by Glaser, and starring Shaquille O'Neal as the title character, a 5,000-year-old genie who appears from a magic boombox to grant a boy three wishes.\n\nTenacious D in The Pick of Destiny: Tenacious D in The Pick of Destiny is a 2006 American musical fantasy comedy film about comedy rock duo Tenacious D.  Written, produced by and starring Tenacious D members Jack Black and Kyle Gass, it is directed and co-written by musician and puppeteer Liam Lynch.  Despite being about an actual band, the film is a fictitious story set in the 1990s about the band's origins, and their journey to find a pick belonging to Satan that allows its users to become rock legends.\n\nForbidden Zone: Forbidden Zone is a 1980 American musical fantasy comedy film directed and produced by Richard Elfman, and co-written by Elfman and fellow Mystic Knights member Matthew Bright.  Originally shot on black-and-white film, the film is based upon the stage performances of the Mystic Knights of the Oingo Boingo.  and revolves around an alternate universe accessed through a door in the house of the Hercules family.\n\nHercules (1997 film): Hercules is a 1997 American animated musical fantasy comedy film produced by Walt Disney Feature Animation for Walt Disney Pictures.  The 35th Disney animated feature film, the film was directed by Ron Clements and John Musker.  The film is loosely based on the legendary hero Heracles (known in the film by his Roman name, Hercules), the son of Zeus, in Greek mythology.  The film also featured the first positive portrayal of African American women in a Disney animated film.\n\nPete's Dragon (1977 film): Pete's Dragon is a 1977 American live-action animated musical fantasy comedy film directed by Don Chaffey, produced by Jerome Courtland and Ron Miller, and written by Malcolm Marmorstein.  It is based on an unpublished short story of the same name, written by classical Hollywood writer Seton I. Miller.  It stars Helen Reddy, Jim Dale, Mickey Rooney, Red Buttons, Shelley Winters, and Charlie Callas.  It revolves around an orphaned boy raised by an abusive hillbilly family who is friends with a dragon named Elliott.\n\nQuestion: What 2006 American musical fantasy comedy film, branched a tour called The Pick of Destiny Tour?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"film_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin for the film.\"\n    },\n    \"related_tour\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"tour_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the tour associated with the film.\"\n        },\n        \"tour_start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The start date of the tour.\"\n        },\n        \"tour_end_date\": {\n          \"type\": \"string\",\n          \"description\": \"The end date of the tour.\"\n        },\n        \"number_of_shows\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of shows in the tour.\"\n        }\n      },\n      \"required\": [\n        \"tour_name\",\n        \"tour_start_date\",\n        \"tour_end_date\",\n        \"number_of_shows\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"film_country_of_origin\",\n    \"related_tour\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "film_country_of_origin": {
        "type": "string",
        "description": "The country of origin for the film."
      },
      "related_tour": {
        "type": "object",
        "properties": {
          "tour_name": {
            "type": "string",
            "description": "The name of the tour associated with the film."
          },
          "tour_start_date": {
            "type": "string",
            "description": "The start date of the tour."
          },
          "tour_end_date": {
            "type": "string",
            "description": "The end date of the tour."
          },
          "number_of_shows": {
            "type": "integer",
            "description": "The total number of shows in the tour."
          }
        },
        "required": [
          "tour_name",
          "tour_start_date",
          "tour_end_date",
          "number_of_shows"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "film_country_of_origin",
      "related_tour"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGarage punk (fusion genre): Garage punk is a rock music fusion genre combining punk rock and garage rock that took shape in the indie rock underground between the late 1980s and early 1990s.  Bands drew heavily from stripped-down 1970s punk rock and Detroit proto-punk, and incorporated numerous other styles into their approach, such as power pop, 1960s girl groups and garage rock, hardcore punk, early blues and R&B, and surf rock.\n\nMetacritic: Metacritic is a website that aggregates reviews of media products: music albums, video games, films, TV shows, and formerly, books.  For each product, the scores from each review are averaged (a weighted average).  Metacritic was created by Jason Dietz, Marc Doyle, and Julie Doyle Roberts in 1999.  The site provides an excerpt from each review and hyperlinks to its source.  A color of Green, Yellow or Red summarizes the critics' recommendations.  It has been described as the video game industry's \"premier\" review aggregator.\n\nNew jack swing: New jack swing or swingbeat is a fusion genre spearheaded by Teddy Riley and Bernard Belle that became popular from the late 1980s into the early 1990s.  Its influence, along with hip hop, seeped into pop culture and was the definitive sound of the inventive black New York club scene.  It fuses the rhythms, samples, and production techniques of hip hop and dance-pop with the urban contemporary sound of R&B.  The new jack swing style developed as many previous music styles did, by combining elements of older styles with newer sensibilities.  It used R&B style vocals sung over hip hop and dance-pop style influenced instrumentation.  The sound of new jack swing comes from the hip hop \"swing\" beats created by drum machine, and hardware samplers, which were popular during the Golden Age of Hip Hop, with contemporary R&B style singing.\n\nAlcest: Alcest is a French band from Bagnols-sur-Cèze, founded and led by Neige (Stéphane Paut).  It began in 2000 as a black metal solo project by Neige, soon a trio, but following the release of their first demo in 2001, band members Aegnor and Argoth left the band, leaving Neige as the sole member.  In 2009 drummer Winterhalter from Les Discrets (and formerly Peste Noire) joined Alcest's studio line-up, after eight years with Neige as the sole full-time member.  Since its creation, Alcest has released five studio albums and a number of EPs and split releases.  Their fourth album, 2014's \"Shelter\", marked a dramatic shift towards a distinctly shoegaze sound, however their latest album \"Kodama\" marks a return to their earlier blackgaze sound.  The band are widely credited with pioneering the blackgaze/post-black metal genre, particularly through their EP \"Le Secret\" released in 2005.\n\nAtlas Plug: Tom Salta writes electronic and orchestral music for films, video games and TV shows.  Atlas Plug (stylised ATlA5 PlUG) is his solo project.  Salta has made the music for video games such as \"\", \"Red Steel\" and \"H.A.W.X.\".  Under the name Atlas Plug, Salta has made music for TV shows such as \"Making of Spider-Man 2\" on HBO, UPN's \"America's Next Top Model\" and MTV's \"Making the Video\".  Atlas Plug music has also been used for many video games such as \"\" (Namco), \"Project Gotham Racing 3\" (Microsoft) and \"ESPN Major League Baseball 2K6\" (Take 2).  Tom is currently working on some new video games and Atlas Plug's second album.  The song \"Truth Be Known\" is also used for DotaCinema's \"Dota 2 Top Plays Weekly\" series of videos on YouTube.\n\nBlackgaze: Blackgaze is a fusion genre combining elements of black metal and shoegazing.  The word is a blend of the names of the two genres, described by \"The Guardian\" as \"the buzz term for a new school of bands taking black metal out of the shadows and melding its blast beats, dungeon wailing and razorwire guitars with the more reflective melodies of post-rock, shoegaze and post-hardcore.\"  According to \"Exclaim! \", blackgaze \"marries the harsh, alien instrumentation of black metal with the mellower, dreamy soundscapes of shoegaze.\"  Influenced by atmospheric black metal bands like Ulver and Summoning, the genre was pioneered by French musician Neige around 2005 through the projects Alcest and Amesoeurs and has risen to prominence with the success of American group Deafheaven.  \"The Guardian\" named Deafheaven \"blackgaze's de facto poster boys, the most likely to open up black metal to an even wider audience\", and \"Exclaim!\"  described their second album \"Sunbather\" – the most critically acclaimed album of 2013 on Metacritic – as seminal to blackgaze.\n\nGothic metal: Gothic metal (or goth metal) is a fusion genre combining the heaviness of heavy metal with the dark atmospheres of gothic rock.  The music of gothic metal is diverse with bands known to adopt the gothic approach to different styles of heavy metal music.  The genre originated during the early 1990s in Europe originally as an outgrowth of death-doom, a fusion of death metal and doom metal.  Lyrics are generally dark and introspective with inspiration from gothic fiction as well as personal experiences.\n\nMetalcore: Metalcore is a fusion genre combining elements of heavy metal and hardcore punk.  The word is a portmanteau of the names of the two genres.  Among other styles blending metal and hardcore, such as crust punk and grindcore, metalcore is noted for its use of breakdowns, which are slow, intense passages conducive to moshing.  Pioneering metalcore bands—such as Integrity, Earth Crisis and Converge, all of which had formed by 1990—are described as leaning more toward hardcore, with their style sometimes being called metallic hardcore, whereas later bands—such as Killswitch Engage, All That Remains, Trivium, As I Lay Dying, Bullet for My Valentine, and Parkway Drive—are described as leaning more towards metal.  Pantera and Sepultura (who influenced Trivium, Atreyu, Bleeding Through and Unearth) have been particularly influential to the development of metalcore in the 2000s, which saw many bands in the genre achieve commercial success.\n\nBlues rock: Blues rock is a fusion genre combining elements of blues and rock.  It is mostly an electric ensemble-style music with instrumentation similar to electric blues and rock: electric guitar, electric bass, and drums, often with Hammond organ.  From its beginnings in the early- to mid-1960s, blues rock has gone through several stylistic shifts and along the way it inspired and influenced hard rock, Southern rock, and early heavy metal.  Blues rock continues to be an influence in the 2010s, with performances and recordings by popular artists.\n\nFolk rock: Folk rock is a music genre combining elements of folk music and rock music.  In its earliest and narrowest sense, the term referred to a genre that arose in the United States and the United Kingdom around the mid-1960s.  The genre emerged from bands such as the Beatles, the Searchers, and the Animals in the UK, and Bob Dylan and the Byrds in the US, who played traditional folk music and songs with rock instrumentation.  The term \"folk rock\" is first noted as being used by the U.S. music press in June 1965 to describe the Byrds' music; the band's debut album was released the same month.\n\nQuestion: Blackgaze is a fusion genre combining elements of black metal and shoegazing, their second album \"Sunbather\", was the most critically acclaimed album of 2013 on which website that aggregates reviews of media products: music albums, video games, films, TV shows, and formerly, books? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"review_aggregator_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the website that aggregates reviews of media products.\"\n    },\n    \"media_product_types\": {\n      \"type\": \"array\",\n      \"description\": \"A list of media product types for which the website aggregates reviews.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album mentioned.\"\n        },\n        \"artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist of the album.\"\n        },\n        \"acclaim_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the album was most critically acclaimed.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"artist\",\n        \"acclaim_year\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"review_aggregator_name\",\n    \"media_product_types\",\n    \"album_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "review_aggregator_name": {
        "type": "string",
        "description": "The name of the website that aggregates reviews of media products."
      },
      "media_product_types": {
        "type": "array",
        "description": "A list of media product types for which the website aggregates reviews.",
        "items": {
          "type": "string"
        }
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album mentioned."
          },
          "artist": {
            "type": "string",
            "description": "The artist of the album."
          },
          "acclaim_year": {
            "type": "integer",
            "description": "The year the album was most critically acclaimed."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the album."
          }
        },
        "required": [
          "album_title",
          "artist",
          "acclaim_year",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "review_aggregator_name",
      "media_product_types",
      "album_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSeizure (Cook novel): Seizure is a 2003 novel by American author Robin Cook which explores the concerns raised by advances in therapeutic cloning.  It debuted at Number 6 on The New York Times Best Seller list on August 3, 2003.  It remained on the best seller list for three weeks.  In November 2004 it appeared on the paperback best seller list.\n\n1636: The Kremlin Games: 1636: The Kremlin Games is a novel in the 1632 series written by Gorg Huff and Paula Goodlett along with Eric Flint.  It is the fourth book in the series to be listed on the New York Times Best Seller list for hardcover fiction.  This book reached number 30 on the NY Times list during a single week in June 2012.  Besides being listed on the NY Times Best Seller list, 1636: The Kremlin Games was also listed on the Locus Hardcovers Bestsellers List for the month of September in 2012 at number 6.\n\nJohn Green (author): John Michael Green (born August 24, 1977) is an American author, vlogger, writer, producer, actor and editor.  He won the 2006 Printz Award for his debut novel, \"Looking for Alaska\", and his sixth novel, \"The Fault in Our Stars\", debuted at number one on \"The New York Times\" Best Seller list in January 2012.  The 2014 film adaptation opened at number one at the box office.  In 2014, Green was included in \"Time\" magazine's list of The 100 Most Influential People in the World.  Another film based on a Green novel, \"Paper Towns\", was released on July 24, 2015.\n\nMidnight in Peking: Midnight in Peking is the true story of the murder of a young British woman in January 1937 Peking written by Paul French.  It was first published by Penguin Australia in association with Penguin China in 2011 and has since been published by Penguin Books in the UK and by Penguin Group USA.  It has appeared on international best seller lists including the \"New York Times\" Best Seller List and the \"South China Morning Post\" Best Seller List.  Additionally the book was adapted for radio by \"BBC Radio 4\".\n\nThe FairTax Book: The FairTax Book is a non-fiction book by libertarian radio talk show host Neal Boortz and Congressman John Linder, published on August 2, 2005, as a tool to increase public support and understanding for the FairTax plan.  Released by ReganBooks, the hardcover version held the #1 spot on the \"New York Times\" Best Seller list for the last two weeks of August 2005 and remained in the top ten for seven weeks.  The paperback reprint of the book in May 2006 contains additional information and an afterword.  It also spent several weeks on the \"New York Times\" Best Seller list.  Boortz stated that he donates his share of the proceeds to charity to promote the book.\n\nWomen Who Run With the Wolves: \"Women Who Run With the Wolves: Myths and Stories of the Wild Woman Archetype\" is a book by Jungian analyst, author and poet Clarissa Pinkola Estés, Ph.D, published in 1992 by Ballantine Books.  It spent 145 weeks on The New York Times Best Seller list over a three-year span, a record at the time.  .  Estés won a Las Primeras Award from the Mexican American Women's Foundation for being the First Latina on the \"New York Times\" Best Seller list.  The book also appeared on other best seller lists, including \"USA Today\", \"Publishers Weekly\", and \"Library Journal\".\n\nList of The New York Times Manga Best Sellers: \"The New York Times\" Best Seller list for manga published in the United States was introduced on March 5, 2009, along with two additional lists for hardcover and paperback graphic novels.  The three lists are grouped under the \"Graphic Books\" category.  Deborah Hoffman, an editor for the Best Seller lists, explained that the term \"Graphic Books\" was selected to create an \"inclusive and expansive\" list which can extend to works of both fiction and non-fiction.  Journalist George Gustines announced, in his introduction of the new lists, \"Comics have finally joined the mainstream.\"  The announcement was made the week the film \"Watchmen\", based on the comic book of the same name, was released in movie theaters throughout the U.S.  The Best Seller lists are printed weekly in \"The New York Times Book Review\" magazine, which is published in the Sunday edition of \"The New York Times\" and as a stand-alone publication.\n\nFancy Nancy: Fancy Nancy is a 2005 children's picture book written by Jane O'Connor and illustrated by Robin Preiss Glasser.  The book spent nearly 100 weeks on the New York Times Best Seller list, launching a series that now numbers upwards of 80 books, selling 30 million volumes.  \"Fancy Nancy\" has been on Publishers Weekly's bestseller list for picture books, was a Children's Book-of-the-Month Club selection and a Junior Library Guild Selection.  It also won a \"Borders 2006 Original Voices\" award and has been translated into 20 languages, including Hungarian and Hebrew.  In April 2012, Nancy was featured in her first chapter book, \"Nancy Clancy: Super Sleuth\".  Books in the \"Fancy Nancy\" series have now spent 330 weeks on the New York Times Best Seller list, and in the fall of 2012, \"Fancy Nancy the Musical\" was produced by Vital Theatre Company in New York City.\n\nThe Fault in Our Stars (film): The Fault in Our Stars is a 2014 American romantic drama film directed by Josh Boone, based on the novel of the same name by John Green.  The film stars Shailene Woodley, Ansel Elgort, and Nat Wolff, with Laura Dern, Sam Trammell, and Willem Dafoe playing supporting roles.  Woodley plays Hazel Grace Lancaster, a sixteen-year-old cancer patient who is forced by her parents to attend a support group, where she meets and subsequently falls in love with Augustus Waters, another cancer patient, played by Elgort.\n\nBrunette Ambition: Brunette Ambition is an autobiographical book by American actress and singer Lea Michele, released on May 20, 2014 by Random House imprint Crown Archetype.  It placed at number three on \"The New York Times\" Best Seller list shortly after its release.  The book also debuted on the U.S. Nonfiction Best Seller list at number nine.\n\nQuestion: Which actress starred alongside Ansel Elgort in a movie based on a \"The New York Times\" Best Seller list book?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the film.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"co_star_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who starred alongside the actress.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"co_star_name\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"source_novel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel the film is based on.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the novel.\"\n        },\n        \"nyt_best_seller_status\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"is_best_seller\": {\n              \"type\": \"boolean\",\n              \"description\": \"Indicates if the novel was a New York Times Best Seller.\"\n            },\n            \"peak_position\": {\n              \"type\": \"integer\",\n              \"description\": \"The highest position the novel reached on The New York Times Best Seller list.\"\n            },\n            \"debut_month_year\": {\n              \"type\": \"string\",\n              \"description\": \"The month and year the novel debuted on the NYT Best Seller list.\"\n            }\n          },\n          \"required\": [\n            \"is_best_seller\",\n            \"peak_position\",\n            \"debut_month_year\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"author\",\n        \"nyt_best_seller_status\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"film_details\",\n    \"source_novel_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who starred in the film."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "co_star_name": {
            "type": "string",
            "description": "The name of the actor who starred alongside the actress."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "co_star_name",
          "release_year"
        ],
        "additionalProperties": false
      },
      "source_novel_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the novel the film is based on."
          },
          "author": {
            "type": "string",
            "description": "The author of the novel."
          },
          "nyt_best_seller_status": {
            "type": "object",
            "properties": {
              "is_best_seller": {
                "type": "boolean",
                "description": "Indicates if the novel was a New York Times Best Seller."
              },
              "peak_position": {
                "type": "integer",
                "description": "The highest position the novel reached on The New York Times Best Seller list."
              },
              "debut_month_year": {
                "type": "string",
                "description": "The month and year the novel debuted on the NYT Best Seller list."
              }
            },
            "required": [
              "is_best_seller",
              "peak_position",
              "debut_month_year"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "title",
          "author",
          "nyt_best_seller_status"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actress_name",
      "film_details",
      "source_novel_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

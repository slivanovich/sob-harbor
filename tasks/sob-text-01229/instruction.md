{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Teddy Bears: The Teddy Bears were an American pop music group.  They were record producer Phil Spector's first vocal group.\n\n(The Best Part of) Breakin' Up: \"(The Best Part of) Breaking Up\" is a song written by Phil Spector, Pete Andreoli and Vince Poncia.  It was first recorded by The Ronettes, produced by Phil Spector and arranged by Jack Nitzsche with Ronnie Spector on lead vocals and with backing vocals by Nedra Talley and Estelle Bennett, ably abetted by Darlene Love and the Blossoms, Bobby Sheen (a.k.a. Bob B. Soxx), and Sonny and Cher.  The song was released in April 1964, the year widely recognized as the group's most successful year, and proved to be the group's third consecutive top forty hit in the US.  The single peaked at number 39 on the U.S. \"Billboard\" Hot 100 and number 43 on the UK Singles Chart.\n\nMarshall Leib: Marshall Leib (January 26, 1939 – March 15, 2002) was one of the original members of The Teddy Bears.  Leib and his high school friend, producer Phil Spector, formed the trio.  Leib performed background harmony vocals and they made a black-and-white film of the song \"To Know Him Is to Love Him\", which became the number one song in the U.S. The Teddy Bears' song has since been covered by many artists such as Dolly Parton and Amy Winehouse, to name a few.\n\n(You're My) Soul and Inspiration: \"(You're My) Soul And Inspiration\" is a song by American pop duo the Righteous Brothers.  It was the group's first hit after leaving their long-time producer Phil Spector.  The song was written by Barry Mann and Cynthia Weil, who also wrote the group's first hit \"You've Lost That Lovin' Feelin'\" along with Phil Spector.  It is the title track of their album.  The single peaked at No. 1 on the US \"Billboard\" Hot 100, and reached No. 15 on the UK Singles Chart.  \"Billboard\" ranked the record as the No. 3 single for 1966.\n\nDarlene Love: Darlene Wright (born July 26, 1941), known by her stage name, Darlene Love is an American popular music singer and actress.  She gained prominence in the 1960s for the song \"He's a Rebel,\" a No. 1 American single in 1962, and was one of the artists who performed on the celebrated Christmas album \"A Christmas Gift for You from Phil Spector,\" produced by Phil Spector in 1963.  She is ranked number 84 among Rolling Stone's 100 Greatest Singers.\n\nA Christmas Gift for You from Phil Spector: A Christmas Gift for You from Phil Spector (originally released as A Christmas Gift for You from Philles Records) is an album of Christmas songs, produced by Phil Spector, and originally released as Philles 45 in 1963.  Spector treated a series of mostly secular Christmas standards to his trademark \"Wall of Sound\" treatment, and the selections feature the vocal performances of Spector's regular artists during this period.  The album peaked at number 13 on \"Billboard\" magazine's special, year-end, weekly Christmas Albums sales chart in December 1963.\n\nBack to Mono (1958–1969): Back to Mono (1958–1969) is a box set (4 compact discs or 5 vinyl LPs) compilation of the recorded work of record producer Phil Spector, through the 1960s, released in 1991 by ABKCO as #7118-2.  The first track, \"To Know Him Is to Love Him,\" released in 1958, features Spector performing as part of the group the Teddy Bears.  Initially a vinyl album-sized package, the box contained a booklet with photographs, complete song lyrics, discographical information, and a reproduction of the essay on Spector by Tom Wolfe, \"The First Tycoon of Teen.\"  The package also contained a small, round, red \"Back to Mono\" pin.\n\nYou've Lost That Lovin' Feelin': \"You've Lost That Lovin' Feelin'\" is a song written by Phil Spector, Barry Mann, and Cynthia Weil.  It was first recorded by the Righteous Brothers in 1964, and was produced by Phil Spector.  Their recording is considered by some music critics to be the ultimate expression and illustration of Spector's \"Wall of Sound\" recording technique.  It has also been described by various music writers as \"one of the best records ever made\" and \"the ultimate pop record\".\n\nTo Know Him Is to Love Him: \"To Know Him Is to Love Him\" is a song written by Phil Spector, inspired by words on his father's tombstone, \"To Know Him Was To Love Him.\"  It was first recorded by the only vocal group of which he was a member, the Teddy Bears.  Their recording spent three weeks at No. 1 on the \"Billboard\" Hot 100 singles chart in 1958, while reaching No. 2 on UK's \"New Musical Express\" chart.  Peter & Gordon and Bobby Vinton later had hits with the song, with its title and lyrics changed to \"To Know You Is to Love You\".  In 1987, the song was resurrected by Dolly Parton, Linda Ronstadt and Emmylou Harris, whose \"Trio\" recording topped the U.S. country singles charts.  The song is in 12/8 time.\n\nSpanish Harlem (song): \"Spanish Harlem\" is a song released by Ben E. King in 1960 on Atco Records, written by Jerry Leiber and Phil Spector, and produced by Jerry Leiber and Mike Stoller.  During a 1968 interview, Leiber credited Stoller with the arrangement; similarly, in a 2009 radio interview with Leiber and Stoller on the \"Bob Edwards Weekend\" talk show, Jerry Leiber said that Stoller, while uncredited, had written the key instrumental introduction to the record.  In the team's autobiography from the same year, \"Hound Dog\", Stoller himself remarks that he had created this \"fill\" while doing a piano accompaniment when the song was presented to Ahmet Ertegun and Jerry Wexler at Atlantic Records, with Spector playing guitar and Leiber doing the vocal.  \"Since then, I've never heard the song played without that musical figure.  I presumed my contribution was seminal to the composition, but I also knew that Phil didn't want to share credit with anyone but Jerry, so I kept quiet.\"\n\nQuestion: Marshall Leib, along with Phil Spector, was part of the vocal group that created what song that reached #1 in 1958?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song that reached number one.\"\n    },\n    \"performing_group\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the vocal group that performed the song.\"\n    },\n    \"chart_performance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"peak_position\": {\n          \"type\": \"integer\",\n          \"description\": \"The highest chart position achieved by the song.\"\n        },\n        \"chart_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the chart where the song peaked.\"\n        },\n        \"year_of_peak\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the song reached its peak position.\"\n        }\n      },\n      \"required\": [\n        \"peak_position\",\n        \"chart_name\",\n        \"year_of_peak\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"key_contributors\": {\n      \"type\": \"array\",\n      \"description\": \"Key individuals from the performing group mentioned in the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the contributor.\"\n          },\n          \"role_in_group\": {\n            \"type\": \"string\",\n            \"description\": \"Their role within the performing group (e.g., original member, producer).\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"role_in_group\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"performing_group\",\n    \"chart_performance\",\n    \"key_contributors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song that reached number one."
      },
      "performing_group": {
        "type": "string",
        "description": "The name of the vocal group that performed the song."
      },
      "chart_performance": {
        "type": "object",
        "properties": {
          "peak_position": {
            "type": "integer",
            "description": "The highest chart position achieved by the song."
          },
          "chart_name": {
            "type": "string",
            "description": "The name of the chart where the song peaked."
          },
          "year_of_peak": {
            "type": "integer",
            "description": "The year the song reached its peak position."
          }
        },
        "required": [
          "peak_position",
          "chart_name",
          "year_of_peak"
        ],
        "additionalProperties": false
      },
      "key_contributors": {
        "type": "array",
        "description": "Key individuals from the performing group mentioned in the context.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the contributor."
            },
            "role_in_group": {
              "type": "string",
              "description": "Their role within the performing group (e.g., original member, producer)."
            }
          },
          "required": [
            "name",
            "role_in_group"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "song_title",
      "performing_group",
      "chart_performance",
      "key_contributors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBenares gharana: Benares gharānā is one of the six most common styles of playing of the Indian tabla.\n\nShankar Ghosh: Pandit Shankar Ghosh (1935 – 22 January 2016) was an Indian tabla player from the Farukhabad gharana of Hindustani classical music.  He was an occasional Hindustani classical singer where he followed the Patiala gharana.\n\nFazal Qureshi: Ustad Fazal Qureshi ( born 13 February 1961) is an Indian tabla player.  Born to the legendary tabla player Alla Rakha, under the guidance of his Guru and father, with the inspiration drawn from his brother, Zakir Hussain, he has developed a unique style that is distinguished for its fine sense of rhythm, versatility and eloquence.  He has expanded his horizons by being involved with other styles of music of the world especially Jazz and Western classical music, and has performed with many well known Jazz musicians.  For the last 16 years he has been associated with Mynta, his world music band based in Sweden.  They have performed all over the world and have released six immensely popular albums.  He teaches tabla to the young talented students in the Ustad AllaRakha Institute of Music near Shivaji Park, Dadar. ,\n\nKishan Maharaj: Pandit Kishan Maharaj (Hindi: किशन महाराज ) (3 September 1923 – 4 May 2008) was an Indian tabla player who belonged to the Benares gharana of Hindustani classical music.\n\nAnubrata Chatterjee: Anubrata Chatterjee (born 1 June 1985) is an eminent Indian tabla player of the Farukhabad gharana of Hindustani classical music.  He is the son of world-renowned tabla maestro, Pt.  Anindo Chatterjee.\n\nArup Chattopadhyay: Pt.  Arup Chattopadhyay is an Indian tabla player.  He was born at Chandannagar, West Bengal.  He started learning tabla at the age of six from his father Pt.  Pankaj Chattopadhyay, who himself is a tabla player of Bengal.  After a few years, he came under the tutelage of world famous tabla maestro Pandit Sankar Ghosh of Farukkhabad gharana with whom he continues to learn.  Gradually he has established himself as a top class accompanist and a formidable soloist.  His performances are admired for their tonal quality, crystal clear sound of \"bols\" (tabla syllables) even at an electrifying speed, and tremendous sense of rhythm and melody.  He was awarded the top-grade by All India Radio and Television (All India Radio and Doordarshan).  His performances with most of the leading artists like Pandit Ravi Shankar, Ustad Ashish Khan, Ustad Shahid Parvez, Ustad Rais Khan, Pandit Rajan and Sajan Mishra, Pandit Ajoy Chakraborty, Pandit Manas Chakraborty, Pandit Viswamohan Bhat, Ustad Rashid khan, Pandit Tejendra Narayan Majumder, Pandit Nayan Ghosh and Pandit Kushal Das among others, has established him as a top-notch accompanist throughout the world.  Since 1998, he has been honored to accompany the living legend Pt.  Ravi Shankar in his tours throughout the U.S., Canada, Europe and India.  He accompanied Pt.  Deepak Chowdhury in his U.K. tour, and Pandit Kartick Seshadri in his U.S., Canada, Australia and Mexico tours.  He is also a highly accomplished tabla teacher and was a professor of tabla at Bharatiya Vidya Bhavan in London.  Since 1998 he has been a visiting lecturer of tabla at the University of California, San Diego.\n\nKumar Bose: Kumar Bose (born 4 April 1953) is an Indian tabla maestro and composer of Indian classical music.  Bose belongs to the Benaras Gharana style of tabla playing.  Having honed his skills under the tutelage of the legendary Pandit Kishan Maharaj, Pandit Bose rose to prominence with his flamboyant performances with Pandit Ravi Shankar.  In addition to his musical abilities, Bose is also an awarded sportsman, a carrom champion, and fluently speaks four languages.  In a career spanning more than four decades,Pandit Kumar Bose has established himself as one of the leading exponents of the tabla and an internationally recognised face in the world of Indian Classical Music.  He received the Sangeet Natak Akademi Award in 2007.\n\nNandan Mehta: Nandan Mehta (26 February 1942 – 26 March 2010) was an Indian tabla player and music teacher from Ahmedabad who belonged to the Benaras Gharana of Hindustani classical music.  He established Saptak School of Music and started Saptak Annual Festival of Music in 1980.\n\nAhmed Jan Thirakwa: Ahmed Jan Thirakwa Khan was an Indian tabla player, commonly considered the preeminent soloist among tabla players of the 20th century, and among the most influential percussionists in the history of Indian classical music.  He was known for his mastery of the fingering techniques and aesthetic values of various tabla styles, technical virtuosity, formidable stage presence, and soulful musicality.  While he had command over the traditional tabla repertoire of various gharanas, he was also distinguished by the way in which he brought together these diverse compositions, his reinterpretation of traditional methods of improvisation, and his own compositions.  His solo recitals were of the first to elevate the art of playing tabla solo to an art in its own right in the popular mind.  His style of playing influenced many generations of tabla players.\n\nFarukhabad gharana: Farrukhabad gharana is one of six prominent playing styles or gharanas of North Indian tabla drums, in Hindustani classical music, and derives its name from Farrukhabad in Uttar Pradesh state.  Some modern disciples of this gharana learn from the prestigious tabla organization known as Tablaniketan.\n\nQuestion: Pandit Kishan Maharaj, was an Indian tabla player of Hindustani classical music, who belonged to which one of the six most common styles of playing of the Indian tabla? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the tabla player.\"\n        },\n        \"instrument\": {\n          \"type\": \"string\",\n          \"description\": \"The instrument played by the artist.\"\n        },\n        \"music_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of music the artist is associated with.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"instrument\",\n        \"music_genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"gharana_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the gharana.\"\n        },\n        \"is_one_of_six_common_styles\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the gharana is one of the six most common styles of playing the Indian tabla.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_one_of_six_common_styles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The direct answer to the question: the name of the gharana.\"\n    }\n  },\n  \"required\": [\n    \"player_info\",\n    \"gharana_info\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the tabla player."
          },
          "instrument": {
            "type": "string",
            "description": "The instrument played by the artist."
          },
          "music_genre": {
            "type": "string",
            "description": "The genre of music the artist is associated with."
          }
        },
        "required": [
          "name",
          "instrument",
          "music_genre"
        ],
        "additionalProperties": false
      },
      "gharana_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the gharana."
          },
          "is_one_of_six_common_styles": {
            "type": "boolean",
            "description": "Indicates if the gharana is one of the six most common styles of playing the Indian tabla."
          }
        },
        "required": [
          "name",
          "is_one_of_six_common_styles"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The direct answer to the question: the name of the gharana."
      }
    },
    "required": [
      "player_info",
      "gharana_info",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

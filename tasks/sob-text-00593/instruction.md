{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLick Life: Lick Life (also known simply as Lizard Lick previously known as Lizard Lick Towing) is an American reality television series that originated as a spin-off of the series \"All Worked Up\" and ran for four seasons on truTV from February 7, 2011, to August 18, 2014.  The show follows Ron and Amy Shirley, Bobby Brantley, and their team of repossession agents in the Raleigh suburb of Wendell, North Carolina, the town that has jurisdiction over the Lizard Lick unincorporated area.  The show is known for frequent fights and brawls that take place during the repossessions of vehicles.\n\nList of Lizard Lick Towing episodes: \"Lizard Lick Towing\" is an improvised American reality television series.  It is filmed in the style of cinéma vérité, and the network behind the show, truTV, state that their series \"feature real-life situations,\" unlike other reality shows \"which often involve contests or other highly staged events.\"  The show is a spin-off of the truTV series \"All Worked Up\", and follows Ron Shirley, his wife Amy, Bobby Brantley, and their team of repossession agents in Wendell, North Carolina (the town that has jurisdiction over the \"Lizard Lick\" unincorporated area).\n\nMeliah Rage: Meliah Rage are an American power metal band from Boston, formed in 1987 by guitarist/songwriter Anthony Nichols.  They are characterized primarily as thrash metal with more classical metal melodies.  The band has released seven albums.  Its current members includes Anthony Nichols, Jim Koury, Darren Lourie, Marc Lopes and Stu Dowie.  They at one time featured Godsmack front man Sully Erna on drums, who appeared on the Unfinished Business LP.\n\nPooja Misrra: Pooja Mishra (also written as Pooja Misrra) is a model, Video Jockey, and has also been featured in an item number in a Bollywood movie \"Mera Dil Leke Dekho\" (2006).  Pooja featured in the reality television show \"Big Switch\" on the channel UTV Bindass (2010).  Pooja was in the reality television show \"Bigg Boss 5\" for 8 weeks inside the house on the channel Colors.  Day 67 Pooja re-entered the \"Big Boss 5\" house again but this time as Andrew Symonds's translator (2011).\n\nBack to Reality (TV series): Back to Reality was a reality television show featuring stars from previous reality television programmes.  The show was broadcast on Channel 5 between 15 February 2004 to 5 March 2004.  It was advertised by Channel 5 as being \"The biggest reality show of all time\" however in terms of ratings, it failed to deliver.  The 12 contestants spent 3 weeks in a studio built mansion, with no natural sunlight.  In the final two weeks, the public voted for their favourite housemate with the two people with the lowest votes every 3/4 nights being put to the housemate vote, where the other contestants has to vote for who they wanted to leave.  The show was presented by Tess Daly and Richard Bacon, the first and only series of the show finished with James Hewitt winning the show ahead of Maureen Rees and Craig Phillips.\n\nKhia: Khia Shamone Finch ( ; born Khia Shamone Chambers, November 8, 1970), better known as just Khia, is an American rapper, songwriter, singer, and record producer.  She is best known for her hit single \"My Neck, My Back (Lick It)\".  To date Khia has collectively sold over 2 million records worldwide.\n\nThe Biggest Winner: The Biggest Winner (Arabic: الرابح الأكبر‎ ‎ ) is an Arabic reality television show that began broadcasting on MBC 1 in 2006.  Filming took place in Lebanon.  The show is an adaptation of the American reality television show \"The Biggest Loser\".  The show features a host, personal trainers, and a dietitian who help the contestants lose weight.  As of December 2009, MBC 1 has presented four seasons of the show with a total of 58 contestants from 14 different Arabic countries.\n\nHow I'm Livin': How I'm Livin' is a reality television show on BET.  Each week, the show profiled a couple of big names in the entertainment industry and followed them on their activities for a day.  They have included those on Steve Harvey, LisaRaye, Khia, Tweet, Rickey Smiley, A.J. and Free from \"106 & Park\", and Guy Torry to name a few.\n\nThe Joe Schmo Show: The Joe Schmo Show is a reality television hoax show created by Paul Wernick and Rhett Reese.  The series is broadcast in the U.S. on the cable network Spike.  The show's premise is that a target person or persons are led to believe that they are contestants on a reality television show; in reality, all of the other participants in the purported show – including the host – are actors, and their actions and the outcome of the purported show are all scripted in an attempt to elicit comedic reactions from the targets.  The show's first season, The Joe Schmo Show, aired in 2003, and its second season, Joe Schmo 2, aired in 2004.  The first season's hoax was conducted as a typical reality competition show while the second hoax was a \"Bachelor\"-like dating series.\n\nTush (band): TUSH were an English rock band from London active during the mid-1970s, and at one time featured Def Leppard, Man Raze and Delta Deep guitarist Phil Collen.\n\nQuestion: What network does a reality television show run on that one time featured the singer of the song \"My Neck, My Back (Lick It)?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the reality television show.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network on which the show runs.\"\n    },\n    \"featured_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist featured on the show.\"\n        },\n        \"known_for_song\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song the artist is best known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_for_song\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"show_name\",\n    \"network\",\n    \"featured_artist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_name": {
        "type": "string",
        "description": "The name of the reality television show."
      },
      "network": {
        "type": "string",
        "description": "The television network on which the show runs."
      },
      "featured_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist featured on the show."
          },
          "known_for_song": {
            "type": "string",
            "description": "The title of the song the artist is best known for."
          }
        },
        "required": [
          "name",
          "known_for_song"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "show_name",
      "network",
      "featured_artist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

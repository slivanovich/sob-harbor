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
Nassau County Aquatic Center: The Nassau County Aquatics Center is an aquatic facility in East Meadow, NY.  It is considered the largest Olympic-sized single-tank pool in North America.  At least 16 world records in swimming have been set in the facility.  It was built in 1998 for the Goodwill Games.  Since the Goodwill Games in 1998, it has hosted numerous swimming championships and high level competitions including the USA Swimming National Championship, NCAA National Championship, and FINA World Cup.  The Center is 80,000 square feet with a 68m pool and three moveable bulkheads to accommodate SCM, SCY, and LCM competition.  In 2002, Natalie Coughlin set multiple world records during the FINA World Cup at the center.  In 2002 it was reported that the pool had lost millions of dollars.  Dave Ferris was aquatics director in 2002, he reportedly questioned the reported losses, stating that "I don't believe expenses on the building are completely clear at this time".  In 2011, the facility underwent a renovation after a 40lbs light fixture fell about 55 feet into the swimming pool.  Since 2011 it had also been proposed to build an additional outdoor 50m pool adjacent to the existing facility.

Ted Turner: Robert Edward "Ted" Turner III (born November 19, 1938) is an American media mogul and philanthropist.  As a businessman, he is known as founder of the Cable News Network (CNN), the first 24-hour cable news channel.  In addition, he founded WTBS, which pioneered the superstation concept in cable television.

Goodwill Games: The Goodwill Games was an international sports competition created by Ted Turner in reaction to the political troubles surrounding the Olympic Games of the 1980s.  In 1979, the invasion of Afghanistan caused the United States and other Western countries to boycott the 1980 Summer Olympics in Moscow, an act reciprocated when the Soviet and other Eastern Bloc countries (with the exception of Romania) boycotted the 1984 Summer Olympics in Los Angeles.

1998 Goodwill Games: The 1998 Goodwill Games was the fourth edition of the international sports competition the Goodwill Games, which were created by Ted Turner in reaction to the political troubles surrounding the Olympic Games of the 1980s.  The competition was held in and around New York City in the United States from July 19 to August 2, 1998.  Some events were held in New York City, while many were held in nearby suburbs in Long Island, including Uniondale.

Swimming at the Goodwill Games: Swimming was one of the sports at the quadrennial Goodwill Games competition.  Swimming competitions were held at every one of the five Goodwill Games.  The final swimming events were held at the Games in 2001 as the 2005 edition of the Games were cancelled.

Sudhir Chaudhary (journalist): Sudhir Chaudhary is an Indian Journalist.  He serves as the Editor-in-Chief of Hindi news channel Zee News, In April 2017, he was elevated as the Editor-in-Chief of English news channel World is One News, and Business channel Zee Business by Zee Media Corporation Limited.  Chaudhary raised to prominence by hosting Daily News and Analysis show aired on Zee News.  Chaudhary's tenure as a Chief Editor is known for increasing viewership of his edited news channels.  Chaudhary significantly raised the viewership of Global Indian English News channel World is one news (WION). Chaudhary holds a unique achievement of being an Editor-in-Chief of Hindi and English News Channel, Business Channel at once.  He is considered to be one of the most efficient Chief editor of News Media in India

Judo at the Goodwill Games: Judo was one of the sports at the quadrennial Goodwill Games competition.  Judo competitions were held at three of the five Goodwill Games, with it featuring for a final time at the Games in 1994.

Athletics at the Goodwill Games: Athletics was one of the sports at the quadrennial Goodwill Games competition.  Athletics competitions were held at every one of the five Goodwill Games.  The final athletics events were held at the Games in 2001 as the 2005 edition of the Games were cancelled.

Dawn News: Dawn News is one of Pakistan's 24-hour Urdu news channel.  Based in Karachi, the station is a subsidiary of Pakistan Herald Publications Limited (PHPL), Pakistan's largest English-language media group.  The test transmission of the station occurred on 25 May 2007, and the channel went live on 23 July 2007.  Originally in English, on 15 May 2010, Dawn News converted into an Urdu news channel after successful test transmission of four hours a day.  The conversion was mainly due to its financial crisis and thin viewership in the country.  Express 24/7 replaced it as Pakistan's only English news channel briefly, until it too was shut down by Express Media Group for financial reasons.

Gregory Edgelow: Greg Edgelow (born February 10) is a retired freestyle wrestler from Canada and is a nationally certified Wrestling Coach and Aboriginal Coach with Cree Heritage.  He represented Canada at the 1992 Summer Olympics in Barcelona, Spain and won a bronze medal at the 1990 Goodwill Games in Seattle, two bronze medals at the 1991 Pan American Games in Havana, Cuba and a gold medal at the 1994 Commonwealth Games in Victoria.  He is an eight-time Canadian senior champion (7 Freestyle and 1 Greco).  Edgelow is the only Canadian to win a medal in wrestling (bronze) at the Goodwill Games ever.  He is also the only Canadian wrestler to win four separate consecutive senior weight classes in Freestyle (82 kg, 90 kg, 96 kg, 100 kg).  His last national title was in 1998, the same year that he represented Canada at the World Championships in Tehran, Iran.

Question: Which news channel did the creator of the Goodwill Games found?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_name": {
      "type": "string",
      "description": "The name of the person who created the Goodwill Games."
    },
    "founded_channels": {
      "type": "array",
      "description": "A list of channels founded by the creator.",
      "items": {
        "type": "string"
      }
    },
    "news_channel_name": {
      "type": "string",
      "description": "The name of the news channel founded by the creator of the Goodwill Games."
    }
  },
  "required": [
    "creator_name",
    "founded_channels",
    "news_channel_name"
  ],
  "additionalProperties": false
}

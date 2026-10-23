{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMaroon 5: Maroon 5 is an American pop rock band that originated in Los Angeles, California.  It currently consists of lead vocalist Adam Levine, keyboardist and rhythm guitarist Jesse Carmichael, bassist Mickey Madden, lead guitarist James Valentine, drummer Matt Flynn and keyboardist PJ Morton.\n\nLiving Things World Tour: The Living Things World Tour was the eighth concert tour by American alternative metal band Linkin Park.  It was launched in support of Linkin Park's fifth studio album \"Living Things\" (2012).  The tour was officially announced in April 2012 through a teaser released after the release of trailer of the 11th Annual Honda Civic Tour by Linkin Park and Incubus.  Later tour was officially announced during the Honda Civic Tour.  Its first leg under the name \"Living Things South American Tour\" began on October 5, 2012 in Buenos Aires and ended on October 12, 2012 in Porto Alegre.  Two shows during the whole tour were cancelled.  Both the shows were in Brazil.  The following statement was issued on the official site: \"Due to logistical issues, some changes have been made to Linkin Park's upcoming Brazilian tour.\n\n16th Annual Honda Civic Tour: The 16th Annual Honda Civic Tour was a concert tour headlined by American rock band OneRepublic.  Sponsored by Honda and produced by Marketing Factory, the tour also features Fitz and The Tantrums and James Arthur.  The tour began on July 7, 2017 in Kansas City and concluded on September 27, 2017 in Shanghai.\n\n10th Annual Honda Civic Tour: The 10th Annual Honda Civic Tour was a concert tour co-headlined by American pop punk trio Blink-182 and American rock band My Chemical Romance (in what turned out to be their final tour).  Joined by supporting acts Matt & Kim, Manchester Orchestra, and Rancid, the tour began from August 5, 2011 and ran until October 8.\n\n12th Annual Honda Civic Tour: The 12th Annual Honda Civic Tour was a concert tour headlined by American pop rock band Maroon 5, alongside special guest, American pop rock singer Kelly Clarkson.  Sponsored by Honda Motor Company, the tour also featured Rozzi Crane and \"The Voice\" second season contestant Tony Lucca, as well as American R&B singer PJ Morton as its supporting acts.  With 34 dates, the 12th installment of the tour was the longest, which began on August 1, 2013, in Maryland Heights, Missouri at the Verizon Wireless Amphitheater and ended on October 6, 2013, at the Hollywood Bowl in Los Angeles.\n\nHonda Civic Tour: The Honda Civic Tour is an annual concert tour, sponsored by American Honda Motor Company and produced by Marketing Factory.  Since 2001, each year's headlining band customizes a Honda Civic that is given away to a fan.\n\nInto the Wild Tour: The Into the Wild Tour (also known as Hurricane Tour and the Closer to the Edge Tour) was the second worldwide concert tour by American rock band Thirty Seconds to Mars in support of the band's third studio album, This Is War.  The tour reached the Americas, Europe, Africa, Asia and Australasia over a two-year period and it marks the first major concert tour the band has performed in North America and Australia.  Along with playing arenas and amphitheatres, the tour headlined at several festivals in Europe and Australia.  The tour's namesake derives from a song entitled, \"The Mission\", that appears on the band's eponymous debut album.\n\n13th Annual Honda Civic Tours: The 13th Annual Honda Civic Tours was a concert tour that showcasing three distinct genres of music, as well as becoming a significant pillar of the new Honda Stage music platform.  Alternative rock bands Grouplove and Portugal.  The Man co-headlined the first tour which kicked off on August 10, 2014, in Seattle.  This tour included support acts Typhoon and Tokyo Police Club on various dates.  The second of three tours with Brooklyn-based pop/rock band American Authors began on October 1, 2014.  Support for the second tour included Echosmith, The Mowgli's and Oh Honey on select dates.  Additionally, Latin DJ trio 3BallMTY will headline the final tour of the series which began in mid-November and ran through December 21, 2014.\n\n2010 Summer Tour EP: 2010 Summer Tour is an EP that features the American rock band Paramore, Canadian indie rock band Tegan and Sara, American rock band New Found Glory, and Swedish band Kadawatha.  The EP was sold during the 2010 Honda Civic Tour and the remaining dates of Paramore's Brand New Eyes World Tour.\n\n11th Annual Honda Civic Tour: The 11th Annual Honda Civic Tour was a concert tour co-headlined by the American alternative metal bands Linkin Park and Incubus.  They were joined by Mutemath, a supporting act for the tour.  The tour started on August 10, 2012 and ended on September 10th, 2012.\n\nQuestion:  The 12th Annual Honda Civic Tour was a concert tour headlined by an American pop rock band that originated in what city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tour_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the concert tour.\"\n    },\n    \"headlining_band\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that headlined the tour.\"\n    },\n    \"band_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The musical genre of the headlining band.\"\n    },\n    \"band_origin_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the headlining band originated.\"\n    }\n  },\n  \"required\": [\n    \"tour_name\",\n    \"headlining_band\",\n    \"band_genre\",\n    \"band_origin_city\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tour_name": {
        "type": "string",
        "description": "The name of the concert tour."
      },
      "headlining_band": {
        "type": "string",
        "description": "The name of the band that headlined the tour."
      },
      "band_genre": {
        "type": "string",
        "description": "The musical genre of the headlining band."
      },
      "band_origin_city": {
        "type": "string",
        "description": "The city where the headlining band originated."
      }
    },
    "required": [
      "tour_name",
      "headlining_band",
      "band_genre",
      "band_origin_city"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

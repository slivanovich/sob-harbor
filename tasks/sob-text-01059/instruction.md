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
Okko: Okko is a comic book published in a series of mini-series, or cycles.  Originally published in France by Delcourt, Archaia Studios Press started reprinting the series in English in 2006.  This series is intended for Mature Readers; it contains adult content, graphic violence, and nudity.

Bob Anderson (runner): Bob Anderson (born December 28, 1947, in Manhattan, Kansas) is an American runner, photographer, publisher and film producer.  He has been running for 53 years.  In 2012 he ran 50 races (350.8 miles) to celebrate 50 years of running.  He averaged 6:59/mile.  A movie called "A Long Run" covers the event.  He is the founder of "Runner's World" magazine.  A desire to find information about running and racing led him to a career in magazine and book publishing for more than twenty years.  After selling "Runner's World" to Rodale Press in 1984, he founded "Ujena Swimwear", and "Around Town Productions".  He has been the subject of media coverage for more than forty years.  In 2012 he founded a new sport called Double Racing - a two-stage running race with a halftime recovery break between the legs.

An Inconvenient Truth (book): An Inconvenient Truth: The Planetary Emergency of Global Warming and What We Can Do About It is a 2006 book by Al Gore released in conjunction with the film "An Inconvenient Truth".  It is published by Rodale Press in Emmaus, Pennsylvania, in the United States.

Men's Health: Men's Health ("MH"), published by Rodale Inc. in Emmaus, Pennsylvania, United States, is the world's largest men's magazine brand, with 40 editions in 47 countries.  It is also the best-selling men's magazine on U.S. newsstands.  Although originally started as a men's health magazine, it currently covers various men's lifestyle topics such as fitness, nutrition, fashion, and sexuality.  The magazine's website, MensHealth.com, averages 38 million page views a month.

Women's Health (magazine): Women's Health, published by Rodale in Emmaus, Pennsylvania, is a magazine focusing on health, nutrition, fitness, sex, and lifestyle.  It is published 10 times a year in the United States and has a circulation of 1.5 million readers.  The magazine has 13 international editions spanning 25 countries and reaching more than 8 million readers globally.

MH-18 (magazine): MH-18, published by Rodale Press, was a magazine covering teen lifestyle.  The magazine was started as a quarterly publication in August 2000.  A youth-oriented version of "Men's Health" magazine, it was targeted at 13- to 18-year-old males.  The last issue was published on 12 November 2001.

My Prison Without Bars: My Prison Without Bars is Pete Rose's autobiography, published by Rodale Press on January 8, 2004.

Blackstone Press: Blackstone Press Limited is now a subsidiary of Oxford University Press.  Blackstone Press was a legal publisher.  It was established in March 1988 by Alistair McQueen.  Its management was formerly that of Financial Training Publications, whose law list it purchased.  Blackstone Press started from the best position possible because of that purchase.  The list included "everyday" reference works, and works that were "essential reading" for examinations of the Law Society and Bar and which had been used for that purpose for seven years.  The books published by Blackstone Press were updated and revised incessantly.  In 2000, Blackstone Press had a revenue of £5 million and a net income of £758k.  In 2001, its backlist contained over four hundred books.  The company was purchased from BPP plc by Oxford University Press, becoming a subsidiary of the latter on 14 August 2001.

Georgia Rickard: Georgia Rickard is an Australian-born journalist, magazine editor, author and media commentator.  Her work has appeared in magazines and newspapers across numerous publications both within Australia and globally, for titles such as "Cosmopolitan", "CLEO", "Women's Health", "GQ", "Prevention", and the "Sunday Telegraph".

Prevention (magazine): Prevention is an American healthy lifestyle magazine, started in 1950, and published by Rodale Press in Emmaus, Pennsylvania, in the United States.  The range of subjects includes food, nutrition, workouts, beauty, and cooking.  It was founded by J. I. Rodale and is currently led by Editorial Director Anne Alexander.  It is one of the largest magazines in the world, with a circulation of 2 million editions around the world, and over 10,000,000 readers a month.  The last edition of the Australian version of "Prevention" was published in December 2016.

Question: What year was the magazine Georgia Rickard has written for that is published by Rodale Press started?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the magazine."
    },
    "start_year": {
      "type": "integer",
      "description": "The year the magazine was started."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author who wrote for the magazine."
    }
  },
  "required": [
    "magazine_name",
    "publisher",
    "start_year",
    "author_name"
  ],
  "additionalProperties": false
}

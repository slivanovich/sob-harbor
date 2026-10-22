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
Asuravithu (2012 film): Asuravithu (Malayalam: അസുരവിത്ത്‌ ) is a 2012 Malayalam action film written and directed by A. K. Sajan, starring Asif Ali and Samvrutha Sunil in the lead roles.  The film is a sequel to 2012 film Stop Violence.  The film opened to negative critical reviews and wasn't noticed in the box office either.

22 Jump Street: 22 Jump Street is a 2014 American action comedy film directed by Phil Lord and Christopher Miller, written by Jonah Hill, Michael Bacall, Oren Uziel and Rodney Rothman and produced by and starring Hill and Channing Tatum.  It is the sequel to the 2012 film "21 Jump Street", based on the television series of the same name.  The film was released on June 13, 2014, by Columbia Pictures and Metro-Goldwyn-Mayer.  The film received positive reviews and earned over $331 million at the box office.

Kyaa Kool Hain Hum 3: Kya Kool Hain Hum 3 is a 2016 Indian adult comedy film starring Tusshar Kapoor, Aftab Shivdasani and Mandana Karimi in lead roles along with Gizele Thakral, Claudia Ciesla, Krishna Abhishek, Shakti Kapoor, Darshan Jariwala in pivotal roles.  It was released on January 22, 2016.  The film is a sequel to 2012 film "Kyaa Super Kool Hain Hum" and the third installment of "Kyaa Kool Hain Hum film series".  The film did moderately well at the indian box office.

Waiting for Summer: Waiting for Summer is a 2012 Canadian drama film directed by Senthil Vinu and produced by Krzysztof Pietroszek, starring Caleb Verzyden and Virginia Leigh.  The film was released on March 30, 2012 at the Canadian Film Fest in Toronto, Canada and won the 2012 Film North Best Feature Award at the Film North – Huntsville International Film Festival.

Atlas Shrugged Part III: Who Is John Galt?: Atlas Shrugged Part III: Who Is John Galt?  is a 2014 American science fiction drama film based on Ayn Rand's novel "Atlas Shrugged".  It is the third installment in the "Atlas Shrugged" film series and the sequel to the 2012 film "", continuing the story where its predecessor left off.  The release, originally set for July 4, 2014, occurred on September 12, 2014.  The film used a completely different cast and crew from the first two in the series.

The Three Little Stooges: The Three Little Stooges is an upcoming American action comedy film based on the iconic comedy team The Three Stooges.  The film is a somewhat prequel to the 2012 film "The Three Stooges", and is set to release in 2018.  It is currently unknown if 20th Century Fox will distribute the film as it did with the 2012 film.

Run for Your Wife (2012 film): Run for Your Wife is a UK-made 2012 film, based on the theatre farce "Run for Your Wife", written by Ray Cooney, who along with John Luton also directed the film.  Upon release the film was savaged by critics and has been referred to as one of the worst films of all time, after it grossed just £602 in its opening weekend at the British box office to its £900,000 budget.  It was released on 14 February 2013.

Dybbuk box: The dybbuk box, or dibbuk box (in the Hebrew language known as , or "Kufsat Dibbuk"), is a wine cabinet which is said to be haunted by a dybbuk.  A dybbuk is a restless, usually malicious, spirit believed to be able to haunt and even possess the living.  The box gained notoriety when it was auctioned on eBay with an accompanying horror story written by Kevin Mannis, and is the original inspiration for the 2012 film "The Possession".

The Possession: The Possession is a 2012 American supernatural horror film directed by Ole Bornedal and produced by Sam Raimi.  It was released in the US on August 31, 2012, with the film premiering at the Film4 FrightFest.

Project GoGo Boy: Project GoGo Boys is a 2012 film directed by Jake Jaxson and produced by CockyBoys Studios, a gay pornographic film studio as a tribute to reality television shows.  It chronicles the lives of gay nightclub performers (go-go boys) fighting their way to what is called the "top box".  Critics considered the film as genre-bending, and blurring the lines between reality, performance arts and pornography sex .

Question: Who produced the 2012 film based on the Dybbuk box?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "inspiration_source": {
          "type": "string",
          "description": "The object or story that inspired the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "inspiration_source"
      ],
      "additionalProperties": false
    },
    "producer_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's producer."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The direct answer to the question: the name of the producer."
    }
  },
  "required": [
    "film_details",
    "producer_info",
    "answer"
  ],
  "additionalProperties": false
}

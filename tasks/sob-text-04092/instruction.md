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
Hawa (film): Hawa (English translation - Wind) is a 2003 Hindi horror film starring Tabu.  The film was an unofficial remake of the 1983 American horror film "The Entity" which starred Barbara Hershey.  Hawa was later dubbed into Telugu as "Naa Intlo Oka Roju" and then in Tamil as "Raja Leelai".

The Amazing Colossal Man: The Amazing Colossal Man (aka The Colossal Man) is a 1957 black-and-white science fiction film, directed by Bert I. Gordon and starring Glenn Langan.  It was released in 1957 on a double bill with "Cat Girl" (1957).  The film revolves around a man who grows to over 60 feet tall as the result of an atomic accident.  It is an uncredited adaptation of the 1928 Homer Eon Flint short novel "The Nth Man".

Veedevadandi Babu: Veedevadandi Babu is a 1997 Telugu horror film written and directed by EVV Satyanarayana.  The film is an unofficial remake of Tamil film "Ullathai Allitha", which itself is influenced by the Hindi film Andaz Apna Apna.  The film stars Mohan Babu, Shilpa Shetty, and Tanikella Bharani.  Bangla dubbed as "Amar Pratiggya"

Jenma Natchathiram: Jenma Natchathiram (தமிழ்: ஜென்ம நட்சத்திரம், English: Birth Star) is a 1991 Tamil supernatural horror film directed and Screenplays by Thakkali Srinivasan for Thirai Gangai Films.  The film dialogue were written by Ma.  Pandarinathan, and story were written by Krishnan respectively.  Music by Premi - Srini assets to the soundtrack.  It Stars Baby Vichithra played titular role with Pramoth, Sindhuja and Vivek played pivotal role.  The film was unofficial remake of "The Omen", 1976 British/American supernatural horror drama film directed by Richard Donner.

Cat Girl: Cat Girl is a 1957 British-American film.  It was an unofficial remake of "Cat People" (1942).  American International Pictures released the film in the US as a double feature with "The Amazing Colossal Man".

Papi Gudia: Papi Gudia (English: "Sinful Doll") is a 1996 Hindi horror film directed by Lawrence D'Souza, starring Karisma Kapoor, Avinash Wadhavan, Tinnu Anand and Shakti Kapoor in the lead roles.  The film is heavily inspired by Hollywood film series "Child's Play" and is an unofficial remake of the first "Child's Play" film (1988).  The film flopped heavily at the box office.

Cat People (1942 film): Cat People is a 1942 horror film produced by Val Lewton and directed by Jacques Tourneur.  DeWitt Bodeen wrote the original screenplay, which was based on Val Lewton's short story "The Bagheeta", published in 1930.  The film stars Simone Simon, Kent Smith, Jane Randolph and Tom Conway.

Chaos (2005 Dominion film): Chaos is a 2005 American horror film about the rape and murder of two adolescent girls.  It is an unofficial remake of Wes Craven's "The Last House on the Left", with all character names changed and a different ending.  It stars Kevin Gage and was written and directed by David DeFalco.  The film received widespread negative reviews.

Chori Chori: Chori Chori (Hindi: चोरी चोरी; English: "Surreptitiously") is a 1956 Indian Hindi-language romantic comedy film directed by Anant Thakur, with music by Shankar Jaikishan and lyrics by Hasrat Jaipuri and Shailendra.  The film is an unofficial remake of the American film, "It Happened One Night".  Bhagwan Dada, Pran, David, and Johnny Walker have character parts.  This was the last film of Nargis-Raj Kapoor, with Nargis doing one cameo appearance in the Raj Kapoor starrer Jagte Raho.  The music of "Chori Chori" had popular tracks including "Aaja Sanam", "Yeh Raat Bheegi Bheegi" in the voices of Lata Mangeshkar and Manna Dey, "Jahan Mein Jati Hun" by Lata and Manna and "Sawa Lakh Ki Lottery," by Mohammad Rafi.  The movie would later inspire the unofficial 1991 Hindi re-make "Dil Hai Ke Manta Nahin" directed by Mahesh Bhatt and starring Aamir Khan and Pooja Bhatt.  Like 'Chori Chori' it too became a hit.

Aavi Kumar: Aavi Kumar is a 2015 Tamil horror comedy film directed by Kandeepan.  The film stars Udhaya and Kanika Tiwari in the lead roles while Nassar, Jagan and Manobala among others form an ensemble cast.  This movie is an unofficial remake of Mohanlal starrer Vismayathumbathu (2004).  Music for the film was composed by Vijay Antony and Srikanth Deva and the film opened to negative reviews in July 2015.

Question: The 1957 film "Cat Girl" was an unofficial remake of a 1942 horror film directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "remake_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "remake_type": {
          "type": "string",
          "enum": [
            "official",
            "unofficial"
          ]
        }
      },
      "required": [
        "title",
        "year",
        "remake_type"
      ],
      "additionalProperties": false
    },
    "original_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "director": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "year",
        "director"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The director of the original film."
    }
  },
  "required": [
    "remake_film",
    "original_film",
    "answer"
  ],
  "additionalProperties": false
}

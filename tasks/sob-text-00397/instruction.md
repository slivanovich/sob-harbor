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
The Devil Came from Akasava: The Devil Came from Akasava (German: "Der Teufel kam aus Akasava") is a 1971 West German-Spanish adventure-spy film directed by Jesús Franco.

Serenade (Dover song): "Serenade" is a song by the Spanish rock band Dover.  Written by Cristina Llanos, the track was released in 1997 as the first single from the band's second studio album, Devil Came to Me (1997).  This song was the first single that also became his first number one because of its rhythms and catchy chorus.  It is the most chanted song in their concerts, making it an anthem for this group.

The Farmer's Curst Wife: A farmer had a bad woman for his wife, and one day the devil came for her.  They reached Hell, and the gates were shut, so she struck him.  She made life in hell so bad that the devil brought her back to her husband.

The Life of Mammals: The Life of Mammals is a nature documentary series written and presented by David Attenborough, first transmitted in the United Kingdom from 20 November 2002.

3 Generations (nonprofit): 3 Generations is a non-profit film production company that concentrates on documentary films about oppressed peoples.  Founded in 2007 by Jane I. Wells, its mission is "to support survivors of genocide and victims of crimes against humanity by helping them share their stories."  It tells these stories in the belief that it "fosters the healing process and illuminates our common humanity."  3 Generations has produced several films, most notably: "The Devil Came on Horseback", "Tricked, A Different American Dream", the short films "Native Silence", "A System of Justice, "and most recently "Lost in Lebanon" (2017), a documentary about Syrian refugees in Lebanon. "

2 (Dover album): 2 is a compilation album of songs by the Spanish band Dover, released in 2007.  It is a double CD greatest hits compilation from the band including singles: "Serenade", "Devil Came To Me" and "Loli Jackson" and featuring many singles and favourites from their past albums.

Devil Came to Me (Dover song): "Devil Came to Me" is a song by Dover originally released as the opening track on the band's second studio album "Devil Came to Me", which sold over 800,000 copies.

Brian Steidle: Brian Steidle (born 1976) is a former Marine Corps captain, military and security operations expert, and author who had worked on publicizing the Darfur conflict in Sudan.  Steidle wrote a book, "The Devil Came on Horseback", about his experience, which was turned into a documentary film that premiered at Sundance in 2007.

The Devil Came on Horseback: The Devil Came on Horseback is a documentary film by Ricki Stern and Anne Sundberg illustrating the continuing Darfur Conflict in Sudan.  Based on the book by former U.S. Marine Captain Brian Steidle and his experiences while working for the African Union.  The film asks viewers to become educated about the on-going genocide in Darfur and laments the failure of the US and others to end the crisis.

Jane I. Wells: Jane I. Wells is a documentary filmmaker and activist whose films focus on global human rights and social justice issues.  In 2007, she founded 3 Generations, a non-profit organization that uses film to document stories of witness to crimes against humanity.  She has produced over 40 short films including the award-winning shorts "I'm a Victim, Not a Criminal" (2010), "Lost Hope" (2012) and "Native Silence" (2013).  She is also a producer of the feature documentary films "The Devil Came on Horseback" (2007), "Tricked" (2013), "A Different American Dream" (2016), and "Lost in Lebanon" (2017).

Question: The Devil Came on Horseback and The Life of Mammals are examples of what kind of film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_type": {
      "type": "string",
      "description": "The general category or genre of the films identified."
    },
    "identified_films": {
      "type": "array",
      "description": "A list of films from the question, with details confirming their type.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "confirmation_snippet": {
            "type": "string",
            "description": "A direct quote from the context confirming the film's type."
          },
          "associated_people": {
            "type": "array",
            "description": "Names of individuals explicitly mentioned in the context in relation to this film.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "title",
          "confirmation_snippet",
          "associated_people"
        ],
        "additionalProperties": false
      }
    },
    "total_films_identified": {
      "type": "integer",
      "description": "The total number of films identified and detailed."
    }
  },
  "required": [
    "film_type",
    "identified_films",
    "total_films_identified"
  ],
  "additionalProperties": false
}

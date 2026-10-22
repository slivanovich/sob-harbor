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
Saleh Bakri: Saleh Bakri (Arabic: صالح بكري‎ ‎ , Hebrew: סאלח בכרי‎ ‎ ; born 1977) is a Palestinian theater and film actor.  He began his career in the theater.  Saleh is the son of actor and film director Mohammad Bakri, brother of actors Ziad and Adam Bakri.

Beverly Hills Brats: Beverly Hills Brats is a 1989 American comedy film.  Directed by Jim Sotos, the film starred Peter Billingsley, Martin Sheen, Burt Young, Terry Moore, George Kirby, Ruby Keeler (in her final film) and Whoopi Goldberg in a cameo role.

Couples Retreat: Couples Retreat is a 2009 American romantic comedy film directed by Peter Billingsley marking his directorial debut, and written by Jon Favreau, Vince Vaughn, Dana Fox, Curtis Hanson, and Greg Beeman.  Vaughn and Favreau star with Jason Bateman, Faizon Love, Kristin Davis, Malin Åkerman, Kristen Bell, and Jean Reno.  It was released on October 9, 2009, in the United States.  The film was shot mostly on the French Polynesian island of Bora Bora.  This film has been rated PG-13.

The Arab-Hebrew Theater: The Arab-Hebrew Theater is a multilingual theater located in the Old Saraya House in the Old City of Jaffa.  It serves as a stage for two theater companies working independently and together in two languages: Hebrew and Arabic.  The Hebrew company is "Teatron Mekomi (Local Theater)", which was established in 1990 by Yigal Ezrati and Gabi Eldor, and the Arab company is "Al-Saraya", which was established in 1998.  The theater is partially funded by the Ministry of Culture and the Tel Aviv Municipality.  The theater has three arts directors: Mohammad Bakri, Yigal Ezrati, and Gabi Eldor.

Adam Bakri: Adam Bakri comes from a cinematic family; he is the son of Mohammad Bakri, brother of Saleh Bakri and Ziad Bakri.  After completing a bachelor's degree in English literature and theater arts at Tel Aviv University, Bakri trained at New York's Lee Strasberg Theatre and Film Institute.  Shortly after his graduation, he landed the lead role in Hany Abu-Assad's drama thriller, "Omar".

Neil Billingsley: Neil Billingsley is an American former child actor during the seventies and eighties.  His four siblings were also child actors, most notably Peter Billingsley and Melissa Michaelsen.

Mohammad Bakri: Mohammad Bakri (born 1953; Arabic: محمد بكري‎ ‎ , is a Arab-Israeli actor and film director.

Peter Billingsley: Peter Billingsley (born April 16, 1971), also known as Peter Michaelsen and Peter Billingsley-Michaelsen, is an American actor, director, and producer, known for his role as Ralphie in the 1983 movie "A Christmas Story" and as "Messy Marvin" in the Hershey's Chocolate Syrup commercials during the 1970s.  He began his career as an infant in television commercials.

Term Life: Term Life is a 2016 American action-drama based on the graphic novel of the same name.  It is directed by Peter Billingsley from a screenplay by A.J. Lieberman.  The film stars Vince Vaughn, who also produces the film, Hailee Steinfeld, Jonathan Banks, Mike Epps, Jordi Molla, Shea Whigham, William Levy, Taraji P. Henson, Annabeth Gish, and Terrence Howard.  The film was released on April 29, 2016, in a limited release and through video on demand by Focus World.  The film received negative reviews.

Bangladesh Film Directors Association: Bangladesh Film Directors Association is the pan-national trade body of film directors in Bangladesh.  The Bangladesh Film Directors Association’s General Secretary is Badiul Alam Khokon.  Mushfiqur Rahman Gulzar is the president of Bangladesh Film Directors Association.

Question: are Mohammad Bakri and Peter Billingsley both film directors ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_film_directors": {
      "type": "boolean",
      "description": "True if both individuals are film directors, false otherwise."
    },
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "is_film_director": {
          "type": "boolean",
          "description": "True if the person is a film director."
        },
        "notable_directing_work": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of films directed by the person, if mentioned."
        }
      },
      "required": [
        "name",
        "is_film_director"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "is_film_director": {
          "type": "boolean",
          "description": "True if the person is a film director."
        },
        "notable_directing_work": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of films directed by the person, if mentioned."
        }
      },
      "required": [
        "name",
        "is_film_director"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "are_both_film_directors",
    "person_1",
    "person_2"
  ],
  "additionalProperties": false
}

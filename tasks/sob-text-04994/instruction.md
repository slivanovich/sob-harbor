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
Vic Morrow: Victor "Vic" Morrow (February 14, 1929 – July 23, 1982) was an American actor and director whose credits include a starring role in the 1960s television series "Combat! ", prominent roles in a handful of other television and film dramas, and numerous guest roles on television.  Morrow and two child actors were killed in 1982 by a stunt helicopter crash during the filming of "".  Morrow also gained notice for his roles in movies like "Blackboard Jungle" (1955), "God's Little Acre" (1958), "Dirty Mary, Crazy Larry" (1974), and "The Bad News Bears" (1976).

Mohamed Diab: Mohamed Diab is a writer and director whose work often centers on pressing issues concerning Egyptian society.  He is known for his directorial debut film "Cairo 678" "(Les Femmes du bus 678)", which was released a month before the Egyptian revolution and was described by the New York Times as "unmistakably a harbinger of that revolution."  Paulo Coehlo tweeted about the film calling it "brilliant" and saying "it should be mandatory for men, regardless of their religion/culture, to watch it".

Danny Leiner: Danny Leiner is a film director whose credits include "The Great New Wonderful", "Harold & Kumar Go to White Castle", "Dude, Where's My Car? ", "Layin' Low", and "Time Expired".

Margy Kinmonth: Margy Kinmonth is a film and television director whose credits include feature documentary "Revolution - New Art for a New World" (Foxtrot Films Ltd/Arts Alliance), marking the 1917 Russian Revolution, "War Art with Eddie Redmayne" ( 2015), which shows on ITV and Ovation, about artists of the First World War, Bafta nominated feature documentary "Hermitage Revealed" (Foxtrot Films Ltd/Arts Alliance, Moscow International Film Festival 2014), "Royal Paintbox" with HRH the Prince of Wales (Foxtrot Films Ltd/ ITV, MIFF 2013), "Looking for Lowry" with Ian McKellen, Noel Gallagher and Dame Paula Rego (Foxtrot Films/ ITV) ""Mariinsky Theatre," "Nutcracker Story"" and BBC series "Naked Hollywood", winner of BAFTA Best Documentary Series.

The Medallion: The Medallion () is a 2003 American-Hong Kong action-comedy film co-written and directed by Hong Kong filmmaker Gordon Chan, and starring Jackie Chan, Lee Evans, Claire Forlani and Julian Sands.  It was much less successful than Chan's other American movies such as the "Rush Hour" film series, "Shanghai Noon" and its sequel, "Shanghai Knights".  The film was theatrically released on 15 August 2003 in Hong Kong and 22 August 2003 in the United States by TriStar Pictures.

Steve Jaggi: Steve Jaggi is a Canadian film producer and director.  His producing credits include the teen film Rip Tide, which premiered at the 2017 Sydney Film Festival, Embedded, Spirit of the Game, Ambrosia, Circle of Lies, Temptation, the documentary London Tango and the short lived British cable television series Be On TV.  His directing credits include Chocolate Oyster and the documentary And The Beat Goes On.  Jaggi also acts as an executive producer, and his credits include Rough Stuff, Skin Deep, Zelos and Crushed.

Alan Metter: Alan Metter is an American film director whose most notable credits include "Back to School" starring Rodney Dangerfield, and "Girls Just Want to Have Fun" with Sarah Jessica Parker.  He also produced and directed the 1983 television special "The Winds of Whoopie" for Steve Martin.

Mikael Salomon: Mikael Salomon (born 24 February 1955) is a Danish-born cinematographer, director and producer of film and television.  After a long cinematography career in Danish cinema, he transitioned to the Hollywood film industry in the late 1980s and has remained highly prolific there, earning two Academy Award nominations.  He is also an acclaimed and prolific television director whose credits include dozens of series, films and miniseries including "Band of Brothers, Salem's Lot, Rome," and "The Andromeda Strain", for which has received numerous awards and nominations including a Primetime Emmy Award and Directors Guild of America Award.

Tom Dey: Thomas Ridgeway "Tom" Dey (born April 14, 1965) is an American film director, screenwriter, and producer.  His credits include "Shanghai Noon", "Showtime", "Failure to Launch", and "Marmaduke".

Shanghai Noon: Shanghai Noon is a 2000 American-Hong Kong martial arts western comedy film starring Jackie Chan, Owen Wilson and Lucy Liu.  The first in the "Shanghai (film series)".  The film, marking the directorial debut of Tom Dey, was written by Alfred Gough and Miles Millar.

Question: Shanghai Noon was the directorial debut of an American film director whose other credits include Showtime, Failure to Launch, and what other film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the film director."
    },
    "director_nationality": {
      "type": "string",
      "description": "The nationality of the director."
    },
    "directorial_debut_film": {
      "type": "string",
      "description": "The title of the film that was the director's debut."
    },
    "other_known_films_mentioned": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other films directed by this person that were explicitly mentioned in the question."
    },
    "answer_film_title": {
      "type": "string",
      "description": "The title of the film that answers the question."
    }
  },
  "required": [
    "director_name",
    "director_nationality",
    "directorial_debut_film",
    "other_known_films_mentioned",
    "answer_film_title"
  ],
  "additionalProperties": false
}

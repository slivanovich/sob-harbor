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
Seduced and Betrayed: Seduced and Betrayed is a 1995 American television thriller film directed by Félix Enríquez Alcalá.  It stars Susan Lucci, David Charvet, Mary Ellen Trainor & Gabrielle Carteris.  The film debuted on April 24, 1995 on NBC.

The Taking of Pelham One Two Three (1998 film): The Taking of Pelham One Two Three is a 1998 American/Canadian television movie directed by Félix Enríquez Alcalá and starring Edward James Olmos.  It is a television adaptation of the novel of the same name by Morton Freedgood (writing under the pseudonym John Godey), and is a remake of the original 1974 film adaptation.  It was followed by another film remake in 2009.

18th Golden Raspberry Awards: The 18th Golden Raspberry Awards were held on March 22, 1998, at the Hollywood Roosevelt Hotel to recognize the worst the movie industry had to offer in 1997.  This year, the film with the most nominations was "Batman & Robin" with 11, followed by "" with 8 nominations, "Anaconda" with 6 nominations, "The Postman" with 5 nominations (winning all of the awards it was nominated for), and "Fire Down Below" with 4 nominations.  The film that won the most awards was "The Postman", winning in all five categories the movie was nominated for.  The list of nominees follows, with recipients denoted in bold.

The Official Razzie Movie Guide: The Official Razzie Movie Guide: Enjoying the Best of Hollywood's Worst is a book about the Golden Raspberry Awards (Razzies), written by John Wilson, founder of the awards ceremony.  The book was published in 2005 by Warner Books, the same year as the 25th Golden Raspberry Awards.

Fire Down Below (1997 film): Fire Down Below is a 1997 American action film starring Steven Seagal and directed by Félix Enríquez Alcalá in his directorial debut.  The film also includes cameos by country music performers Randy Travis, Mark Collie, Ed Bruce, Marty Stuart and Travis Tritt, and country-rocker and the Band member Levon Helm.  Steven Seagal plays Jack Taggart, an EPA agent who investigates a Kentucky mine and helps locals stand up for their rights.  The film was released in the United States on September 5, 1997.

29th Golden Raspberry Awards: The 29th Golden Raspberry Awards (Razzies) ceremony was held by the Golden Raspberry Awards Foundation to "honor" the worst films of 2008 on February 21, 2009, at the Barnsdall Gallery Theatre in Hollywood, California, USA.  Nominations were announced on January 21, 2009. " The Love Guru" was the most nominated film of 2008, with seven.  Award results were based on votes from approximately 650 journalists, cinema fans and film professionals from 20 countries.  Awards were presented by John Wilson, the ceremony's founder.  "The Love Guru" received the most awards, winning Worst Picture, Worst Actor, and Worst Screenplay.  Paris Hilton received three awards, including Worst Actress for her work in "The Hottie & the Nottie" and Worst Supporting Actress for "Repo!  The Genetic Opera".  Hilton matched the record number of awards received by an actor in a single year, set by Eddie Murphy the previous year at the 28th Golden Raspberry Awards for his roles in "Norbit".

36th Golden Raspberry Awards: The 36th Golden Raspberry Awards ceremony, held by the Golden Raspberry Foundation, recognized the worst films in 2015.  The satirical ten-category Golden Raspberry Awards, commonly known as the "Razzies", were presented during the ceremony.  The nominations were revealed on January 13, 2016.  The ceremony was held on February 27, 2016 beginning at 8:00 p.m. PST at the Palace Theater in Los Angeles.

37th Golden Raspberry Awards: The 37th Golden Raspberry Awards was an awards ceremony that honors the worst the film industry had to offer in 2016.  The Golden Raspberry Awards, also known as the "Razzies", are awarded based on votes from members of the Golden Raspberry Foundation.  The pre-nomination ballots were revealed on the week of January 2, 2017, with the nominations being revealed on January 23, 2017.  The winners were announced on February 25, 2017.

Justice League of America (film): Justice League of America is a 1997 television film and an unsuccessful pilot produced by CBS and directed by Félix Enríquez Alcalá, based on a team of fictional DC Comics superheroes from the comic of the same name.  The film centers on a female meteorologist who gains superpowers and is later inducted into the "Justice League," while the city of New Metro is held for ransom by a terrorist armed with a weather control device.

35th Golden Raspberry Awards: The 35th Golden Raspberry Awards was an awards ceremony that honored the worst the film industry had to offer in 2014.  The Golden Raspberry Awards, also known as "Razzies", are awarded based on votes from members of the Golden Raspberry Foundation.  The pre-nomination ballot was revealed on December 31, 2014, and final nominations were revealed on January 14, 2015.  The winners were announced on February 21, 2015 at a ceremony that was open to the public for the first time in the award's history.

Question: What movie directed by Félix Enríquez Alcalá was nominated for Golden Raspberry Awards in 1998?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie nominated for the award."
    },
    "director": {
      "type": "string",
      "description": "The director of the movie."
    },
    "award_ceremony_year": {
      "type": "integer",
      "description": "The year the Golden Raspberry Awards ceremony was held."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "award_type": {
      "type": "string",
      "description": "The name of the award received or nominated for."
    }
  },
  "required": [
    "movie_title",
    "director",
    "award_ceremony_year",
    "film_release_year",
    "award_type"
  ],
  "additionalProperties": false
}

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
Jongens: Jongens (English title: "Boys") is a 2014 coming of age drama film produced in the Netherlands.  It was directed by Mischa Kamp and features Gijs Blom, Ko Zandvliet and Stijn Taverne.  The film was released on 9 February 2014.

Winona Ryder: Winona Ryder (born Winona Laura Horowitz; October 29, 1971) is an American actress.  One of the most successful and iconic actresses of the 1990s, she made her film debut in the film "Lucas" (1986).  As Lydia Deetz, a goth teenager in Tim Burton's "Beetlejuice" (1988), she won critical acclaim and widespread recognition.  After appearances in film and on television, Ryder continued her acting career with the cult film "Heathers" (1988), a controversial satire of teenage suicide and high school life that has since become a landmark teen film.  She later appeared in the coming of age drama "Mermaids" (1990), earning a Golden Globe Award nomination, and in the same year appeared alongside Johnny Depp in Burton's dark fairy-tale "Edward Scissorhands" (1990), and shortly thereafter with Keanu Reeves in Francis Ford Coppola's gothic romance "Bram Stoker's Dracula" (1992).

Vikramadithyan: Vikramadithyan is a 2014 Malayalam coming of age drama film co-produced and directed by Lal Jose.  The film stars Dulquer Salmaan, Unni Mukundan and Namitha Pramod in the lead roles, while Anoop Menon, Lena, Santhosh Keezhatoor and Joy Mathew appear in supporting roles and Nivin Pauly appears in a guest role.  The screenplay is by Iqbal Kuttippuram, while Jomon T. John handles the cinematography.  The music is composed by Bijibal.  The film was released on 25 July 2014.

Yevade Subramanyam: Yevade Subramanyam (English: "Who is Subramanyam?")  is a 2015 Telugu coming of age drama film directed by debutante film maker Nag Ashwin, starring Nani as the title character, a corporate man who sets out on a journey of self-discovery.  Produced by Priyanka Dutt, and Swapna Dutt the film also features newcomer Malavika Nair, Vijay Deverakonda and Ritu Varma in supporting roles.  Much of the filming took place at the Everest Base Camp, becoming the first Indian film to be shot at the location.  Upon release, the film received highly positive reviews, praising Nani's impeccable performance and the direction.  This film became a Super Hit at the box office and trumped many movies which released around the same time.  It marked Nani's comeback after a dry spell at the box office.

Laura Prepon: Laura Prepon (born March 7, 1980) is an American actress, director, and author.  She is best known for her role as Donna Pinciotti in all eight seasons of the Fox sitcom "That '70s Show" (1998–2006), and for her portrayal of Alex Vause in the Netflix original comedy-drama series "Orange Is the New Black" (2013–present).  Prepon has worked mainly in television.  She made her film debut in 2001 with the independent film "Southlander".  Her other films include the romantic drama "Come Early Morning" (2006), the comedy "Lay the Favorite" (2012), the thriller "The Girl on the Train" (2016), and the drama "The Hero" (2017).

Never Again as Before: Never Again as Before (Italian: Mai + come prima ) is a 2005 Italian coming of age drama film produced, written and directed by Giacomo Campiotti.

Dhanush filmography: Dhanush is an Indian film actor, producer, lyricist and singer known for his work in Tamil cinema.  He made his acting debut in 2002 with the coming of age drama, "Thulluvadho Ilamai", directed by his father Kasthuri Raja.  His role as a mentally-disturbed man in "Kaadhal Kondein" (2003)directed by his brother Selvaraghavanwon him critical acclaim.  The following year, he starred in Subramaniam Siva's "Thiruda Thirudi", a commercial success.  This was followed by a series of commercial failures"Pudhukottaiyilirundhu Saravanan" (2004), "Sullan" (2004) and "Dreams" (2004).  He had two releases in 2005"Devathayai Kanden" and "Adhu Oru Kana Kaalam".

Lightning Bug (film): Lightning Bug is a 2004 coming of age drama film.  It is the debut film by writer/director and SFX makeup artist Robert Green Hall.  The film a fictionalized account of Hall's own childhood and entry into special effects makeup for film and television.  It was filmed on location Fairview, Alabama.  The film was executive produced by Laura Prepon.

Ashley Laurence: Ashley Laurence (born May 28, 1966) is an American actress and artist.  She made her film debut in 1987 by starring as Kirsty Cotton in Clive Barker's "Hellraiser" (1987).  She reprised her role as Kirsty in the sequels "" (1988), "" (1992), and "" (2002).  Her other film roles include "The Lurking Fear" (1994), "Lightning Bug" (2004) and "Red" (2008).  She has been featured in several national advertising campaigns.

Grantham &amp; Rose: Grantham & Rose is a 2014 American independent coming of age drama film directed by Kristin Hanggi and starring Jake T. Austin and Marla Gibbs.  It is Hanggi's directorial debut.  Michael Urie served as an executive producer of the film.

Question: Lightning Bug is a 2004 coming of age drama film executive produced by an American actress best known for her role as who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "executive_producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the executive producer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the executive producer."
        },
        "best_known_role": {
          "type": "string",
          "description": "The role the executive producer is best known for."
        },
        "best_known_role_series_title": {
          "type": "string",
          "description": "The title of the series or film where the executive producer played their best known role."
        }
      },
      "required": [
        "name",
        "nationality",
        "best_known_role",
        "best_known_role_series_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "executive_producer"
  ],
  "additionalProperties": false
}

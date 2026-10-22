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
Ism (film): Ism is a 2016 Telugu action crime thriller film produced by Nandamuri Kalyan Ram under N. T. R. Arts banner and directed by Puri Jagannadh.  Starring Nandamuri Kalyan Ram, Aditi Arya in the lead roles, Jagapati Babu plays an important supporting role and music composed by Anup Rubens.  Junaid Siddiqui, Mukesh G and Johnny Shaik handled the editing, cinematography and Art direction respectively.  It was shot in August 2016 in Valencia, Spain.  The film was released on 21 October 2016.

Kick 2: Kick 2 is a 2015 Telugu action comedy film written by Vakkantham Vamsi and directed by Surender Reddy.  It features Ravi Teja as the protagonist and is the sequel of the 2009 Telugu film "Kick" starring Ravi Teja, which was also directed by Surender Reddy.  The film is produced by actor Nandamuri Kalyan Ram on the N.T.R. Arts banner.  The film was officially launched on 20 August 2014, and the principal photography began on the same day.  The audio soundtrack of the movie was composed by S. Thaman and was released on 9 May 2015.  The film was released worldwide on 21 August 2015 and was produced on a budget of () .  The movie collected around () in its 14-day run It was also dubbed into Hindi as Jigarwala No. 1 .

Nandamuri Kalyan Ram: Nandamuri Kalyan Ram is an Indian actor and film producer who works in Telugu cinema.  He was born to actor and politician Nandamuri Harikrishna and Lakshmi.  He is one of the grandsons of N. T. Rama Rao, who was an actor and a statesman.  Actor Jr.NTR is his Brother.  He is the owner of the production company named after his grandfather late NTR, called N.T.R. Arts.  He had played a lead role in several movies like "Athanokkade", "Hare Ram" and "Pataas".  He also owns a VFX company named "Advitha Creative Studios" which provided special effects for movies like "Legend", "Nannaku Prematho", "Krishnashtami" etc.

Pataas: Kalyan Sinha (Nandamuri Kalyan Ram) is a corrupt IPS officer who gets himself transferred to Hyderabad and misuses his power to gain monetary benefits in unorthodox methods.  During this process, he also encourages a local MP named GK (Ashutosh Rana) who has become a huge headache to Murali Krishna (Saikumar Pudipeddi), the DGP of Andhra Pradesh .  Kalyan happens to be Murali's son who is angry on the latter as his supposed negligence killed his mother and just born sister, though Murali actually left his wife in the hospital to save several families in a riot.  Unaware of this, Kalyan left Murali and joined an orphanage and became an IPS officer to seek revenge on his father.  During his life at Hyderabad, Kalyan also meets two women; Mahathi, (Shruti Sodhi) journalist working for TV5 and Kavya (Prachi Thaker), a deaf-mute philanthropist who works in a coffee shop.  He loves Mahathi and expects her to reciprocate the same only to be rejected by her because of his corrupt nature.  Kavya is killed by GK's brother Nani when she tries to save a techie from being assaulted sexually by him near HITEC City.

Legend (2015 film): Legend is a 2015 French-British crime thriller film written and directed by Brian Helgeland.  It is adapted from John Pearson's book "The Profession of Violence: The Rise and Fall of the Kray Twins", which deals with the rise and fall of the Kray twins; the relationship that bound them together, and charts their gruesome career to their downfall and imprisonment for life in 1969.

Bala Gopaludu: Bala Gopaludu is a 1989 Telugu, Village backdrop film produced by M. R. V. Prasad on P. B. R. Art Productions banner and directed by Kodi Ramakrishna.  Starring Nandamuri Balakrishna, Suhasini in the lead roles and music composed by Raj-Koti.  This film is first debut of Nandamuri Kalyan Ram as child artist.

Hare Ram: Hare Ram is a 2008 Telugu movie directed by Harshavardhan", and produced by Kalyan Ram, under N.T.R. Arts.  Kalyan Ram, Priyamani and Sindhu Tolani play the lead roles while Ali, Brahmanandam, Kota Srinivasa Rao and Raghu Babu play supporting roles.  Mickey J Meyer was the music director, "C. Ram Prasad" handled cinematography, and was edited by "Gowtham Raju".  The film was released on 18 July 2008.  This movie is the next best hit for Kalyan Ram after "Athanokkade" which was a blockbuster.  This film was dubbed into Hindi as Julmo Ka Tandav

Om 3D: Om 3D is a 2013 3D Telugu action film written and directed by Sunil Reddy starring Nandamuri Kalyan Ram.  The film is tipped to be India's first action 3D film.  Nikesha Patel and Kriti Kharbanda are the leading ladies.  The film has been shot in 5k resolution for great visuals.  Hollywood technicians such as David Taylor, who worked for "Avatar" and "Final Destination 5", and Ian Markus, known for films such as "The Amazing Spiderman", have also worked for this film.  The shooting was done in 110 days, but the post production took another year.  Music was composed by Achu Rajamani and Sai Karthik.  The action entertainer, produced under the banner NTR Arts, is slated to release on 19 July.  The film has failed at box office.

N. T. R. Arts: Nandamuri Kalyan Ram established the production house with the name of his grand father, legendary actor and former Chief Minister, Nandamuri Taraka Rama Rao.  The production house has introduced some good directors such as Surender Reddy and Anil Ravipudi to Tollywood.

Jai Lava Kusa: Jai Lava Kusa is a 2017 Indian Telugu-language action-drama film written and directed by K. S. Ravindra.  The movie features Jr.  NTR, Raashi Khanna and Nivetha Thomas in the lead roles.  This film marks the Telugu debut of Hindi film and television actor Ronit Roy, who will play the film's villain.  The movie is produced by Jr.  NTR's brother Nandamuri Kalyan Ram under his banner N. T. R. Arts.  The soundtrack is composed by Devi Sri Prasad.  Chota K. Naidu is the film's cinematographer.

Question: Which company, owned by Nandamuri Kalyan Ram, provided that special effects for a 2015 French-British crime thriller film written by Brian Helgeland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "owner_name": {
      "type": "string",
      "description": "The name of the owner of the company."
    },
    "service_provided": {
      "type": "string",
      "description": "The type of service provided by the company for the film."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "origin": {
          "type": "string",
          "description": "The country/countries of origin for the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "writer": {
          "type": "string",
          "description": "The writer of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre",
        "origin",
        "writer",
        "director"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "owner_name",
    "service_provided",
    "film_details"
  ],
  "additionalProperties": false
}

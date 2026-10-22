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
Dasavatharam (film): Dasavatharam (தமிழ்: தசாவதாரம், English: The Ten Avatars) is a 1976 Tamil Hindu - Devotional Mythology film was directed and script were written by K. S. Gopalakrishnan.  Music by S. Rajeswara Rao assets to the film.  It stars Ravikumar played titular role with Sirkazhi Govindarajan, Jayachitra, Gemini Ganesan, M. R. Radha, P. S. Veerappa, Sowcar Janaki and K. R. Vijaya other actor and actress played portraying supporting role.

Vasundhara Devi: Vasundhara Devi (Tamil: வசுந்தரா தேவி) (1917-1988) was an Indian film actress, trained Bharathanatyam dancer and carnatic singer.  Vasundhara Devi is the only Indian actress to have had an audience with the Pope of the Roman Catholic Church.  She is the mother of popular Indian actress Vyjayanthimala.

Divyanka Tripathi: Divyanka Tripathi Dahiya (born on 14 December 1984) is an Indian actress who works in the Hindi television industry.  Establishing herself as one of the most popular actresses in the industry, she rose to fame by playing a dual role in Zee TV's serial "Banoo Main Teri Dulhann" for which she won the Indian Television Academy Award for Best Actress in the drama category.  Later, she garnered the Indian Telly Award for Best Actress in a Lead Role for portraying the character of Dr. Ishita Raman Bhalla in Star Plus's soap opera "Ye Hai Mohabbatein" and in 2017, she won the dance reality show Nach Baliye.

Malishka RJ: Malishka Mendonsa, popularly known as RJ Malishka , is a radio personality from Mumbai, India.  She works in Red FM 93.5.  Her show "Morning No 1 with Malishka" has won the "Best Breakfast Programme/Show (Hindi) at the Indian Excellence in Radio Awards" in the past.  Actress Vidya Balan was trained by RJ Malishka when the actress played the role of an RJ in 2006 Bollywood film Lage Raho Munnabhai.

Kumari (actress): Nagaraja Kumari Maddela (1921 – 3 March 2008), better known as Kumari, was a renowned south Indian actress, playback singer, musician, beauty queen, and a model.  She was the first Indian actress to play dual-roles in film.  She pioneered the art of playing multiple roles in a single film.  She was also one of the first Indian faces used by Lux (soap), a brand that pioneered female celebrity endorsement, and have since used famous faces such as Aishwarya Rai.

Ambili Devi: Ambili Devi is a South Indian actress who appears in Malayalam Films & Serials.  She has established herself as a lead actress in Malayalam Television Industry and has won the "Kerala state Television Award for Best Actress in 2005". She has acted in over 30 Television soap opera's.

Archana (actress): Archana is an Indian film actress and accomplished Kuchipudi and Kathak dancer, known for her works in the South Indian film industry.

Talluri Rameshwari: Talluri Rameshwari (also known as Rameshwari) is an Indian actress.  She was born and raised in Andhra Pradesh and spent her childhood in Kakinada.  She is the younger of two sisters and has no brothers.  Her elder sister's name is Krishna Kumari.  She also acted in one of the Telugu movies.  They used to live in Munsiff street, near 2-Town police station, Surya rao peta, Kakinada.  She studied 1st standard to 5th standard in City Aided Elementary School.  She studied from 6th to 10th standard in Municipal Girl's High School, Temple street.  During that time they shifted their residence to 50 buildings area, Kakinada.  She used to be so beautiful in her childhood as well as in her adolescence, resembling the veteran Hindi actress Rajshree ( V. Shantaram's daughter).  She grew up speaking Telugu.  She attended and graduated from FTII in 1975.  She became very popular and still remains popular for her two hit Hindi films: "Dulhan Wahi Jo Piya Man Bhaye" (1977) and "Aasha" (1980), the latter earned her a Filmfare Nomination as Best Supporting Actress.  She played the character Seetalu in the hit film "Seetamalakshmi" (1978), directed by K.Vishwanath, for which she received the Nandi Award for Best actress.  Her credits include several other movies include Sunayana, Mera Rakshak, Sharda and others.  She also worked in several films in other languages (Malayalam, Kannada, Bengali, Oriya, Bhojpuri).  She is not a career savvy individual and never really pushed hard to reach her potential.  She is very close and remains close to her family.  She married her FTII class mate and pal, Punjabi actor-producer, Deepak Seth and has two sons Bhaskara Pratap Seth and Surya Prem Seth.  She took a sabbatical from acting to raise her children, but recently returned to acting in films, playing mature roles.  She and her husband produced a Hindi film titled "Hun Farishte Nahin" (1988) and a Punjabi film titled "Mein tuun assin tussin" (2007) based on the Shakespeare play "The Comedy of Errors".  Lately she has been working in television series.

Yamanam: A physically disabled girl Ambili (Archana) is restricted to a wheelchair because of a childhood attack of polio.  Unable to move out of home, she has only to fantasize the exteriors.  She turns terribly introvert, fathoming the truth within and becoming positive towards people.  She is skilled at making models and toys.  She and her widowed mother are gradually sidelined in their own home by her brother Devan and his wife Raji.

Rohini Hattangadi: Rohini Hattangadi (Marathi: रोहिणी हट्टंगडी ) (born 11 April 1951) is an Indian actress.  She has won two Filmfare Awards, one National Film Award, and is the only Indian actress to win the BAFTA Award for Best Actress in a Supporting Role for her performance as Kasturba Gandhi in "Gandhi" (1982).  An alumna of the National School of Drama of New Delhi, Hattangadi had worked mainly in theatre when she made her movie debut with "Arvind Desai Ki Ajeeb Dastaan" in 1978.  Some of her noted cinematic roles were in such art films as "Arth" (1982), "Party" and "Saaransh" (1984).  Hattangadi was mostly offered character roles in mainstream Hindi cinema after her portrayal in "Gandhi", often typecast in mother roles much ahead of her years.  Respected for her acting prowess, she has appeared in over 80 feature films, and is active in theatre and television.

Question: Which Indian actress played the character Ambili in the film Yamanam?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played in the film."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who played the character."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        },
        "known_for_industry": {
          "type": "string",
          "description": "The film industry the actress is known for."
        },
        "dance_forms": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Dance forms the actress is accomplished in."
        }
      },
      "required": [
        "nationality",
        "known_for_industry",
        "dance_forms"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "character_name",
    "actress_name",
    "actress_details"
  ],
  "additionalProperties": false
}

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
The Ren &amp; Stimpy Show: The Ren & Stimpy Show is an American animated series created by John Kricfalusi for Nickelodeon.  The series follows the adventures of title characters Ren, an emotionally unstable chihuahua, and Stimpy, a good-natured, dimwitted cat.  It premiered on August 11, 1991 as one of the original three Nicktoons, along with "Rugrats" and "Doug".  Throughout its run, the show was controversial for its off-color humor, sexual innuendo, dark humor, adult jokes, and violence.  This controversy contributed to the production staff's altercations with Nickelodeon's Standards and Practices department.  The show ended on December 16, 1996, with a total of five seasons and 52 episodes.

Fiji Week: Fiji Week is a week of festivities culminating in Fiji Day on 10 October (the anniversary of Fiji's independence from British colonial rule in 1970) annually.  A different theme is chosen every year, but common elements include religious ceremonies and cultural performances.

Kalyanram Kathi: Kalyan Ram Kathi (Telugu: కల్యాణ్ రామ్ కత్తి) is a 2010 Indian Telugu action-drama film written and directed by Mallikharjun.  It starts Kalyan Ram in the lead role, alongside Shaam, Sana Khan, Saranya Mohan and Kota Srinivasa Rao.  The film gained attention due to a controversy regarding the film's title, "Kathi".  The title was registered under Gunasekhar.  The film was a flop at box office.  This film was dubbed into Hindi as Maut Ki Zanjeer

Absurdist fiction: Absurdist fiction is a genre of fictional narrative (traditionally, literary fiction), most often in the form of a novel, play, poem, or film, that focuses on the experiences of characters in situations where they cannot find any inherent purpose in life, most often represented by ultimately meaningless actions and events that call into question the certainty of existential concepts such as truth or value.  Common elements in absurdist fiction include satire, dark humor, incongruity, the abasement of reason, and controversy regarding the philosophical condition of being "nothing."  Works of absurdist fiction often explore agnostic or nihilistic topics.

God Bless America (film): God Bless America is a 2011 American black comedy film that combines elements of political satire with dark humor.  The film is written and directed by Bobcat Goldthwait, and stars Joel Murray and Tara Lynne Barr.

Crook (film): Crook is a 2010 Indian Hindi adult thriller film popularly known by the title of It's Good to be Bad! .  The film stars Emraan Hashmi, Neha Sharma and Arjan Bajwa in the lead.  It is directed by Mohit Suri and produced by Mukesh Bhatt.  It was released on 8 October 2010.  Before the release, the film was given an 'A' certificate from the Indian Censor Board, due to the erotic scenes between Emraan Hashmi and Shella Allen.  Mostly shot in Australia and South Africa, the film is based on the controversy regarding the allegedly racial attacks on Indian students in Australia between 2007 and 2010.  The film met mixed responses upon its release and went on to become a box office flop.

Criminology (film): Criminology is a 2016 Canadian absurdist film directed by Jeremy Ma and Angus Ng.  The film stars Spencer Cadlick, James Russell and Kasey Ryne Mazak.

Roberta Allen: Roberta Allen is a short story writer, novelist, memoirist, conceptual artist, sculptor, photographer, and creative writing instructor.  Language has been the inspiration for both her writing and her art.  In her conceptual works - which include drawings, collages, artist books, photo/text works, installations and digital prints - she explores how text informs or changes our perception of images, often with more than a hint of humor and a philosophical bent.  With dark humor, her books present characters at odds with themselves and others, sometimes in exotic locales.

Selfie Pod: A Selfie Pod is a modern "open" style photo booth setup used most commonly at parties, weddings and corporate activities.  Such pods are generally custom-made from aluminum and have the appearance of a tower, or pod.  Common elements include either a DSLR camera or webcam, touchscreen computer monitor, and photo printer.

Silvano Melea Otieno: Silvano Melea Otieno (1931 – 20 December 1986) — also known as S.M Otieno and Silvanus Melea Otieno — was a leading criminal lawyer in Nairobi whose death gave rise to a significant legal controversy regarding the tension between customary and common law in Kenya.

Question: What is the title of the Canadian film directed by Jeremy Ma and Angus Ng whose common elements include satire, dark humor, incongruity, the abasement of reason, and controversy regarding the philosophical condition of being "nothing"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "directors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of directors for the film."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the film was produced."
    },
    "genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "genre_elements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Common elements or characteristics of the film's genre."
    }
  },
  "required": [
    "film_title",
    "directors",
    "country_of_origin",
    "genre",
    "genre_elements"
  ],
  "additionalProperties": false
}

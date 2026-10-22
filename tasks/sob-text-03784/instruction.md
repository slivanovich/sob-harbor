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
Volume Up (radio show): Volume Up () is a South Korean radio show currently hosted by Kim Ye-won on KBS 2FM in Seoul and UKBS MUSIC DMB in the provinces, airing everyday at 20:00–22:00 (KST), just right after KBS 2FM News 8PM edition.  Known as the "ruler of the dinner time" the show became the highest-rated radio program in its time slot across both AM and FM bandwidths in Seoul.  KBS 2FM was South Korea's No. 10 station.  Popular for soft music playlist, a short soap opera segment called "Lie to Me" based on the 2011 TV drama of the same title and Yoo's "My Final Message".

Only Love (TV series): Only Love () is a 2014 South Korean daily drama television series starring Seo Ha-joon, Im Se-mi, Lee Kyu-han, Nam Bo-ra, Yoon Jong-hoon, and Kim Ye-won.  It aired on SBS on Mondays to Fridays at 19:20 for 123 episodes from June 2 to December 12, 2014.

Kim Ye-won: Kim Ye-Won (born August 19, 1998), widely known by her stage name Umji, is a south korean singer.  She is best known as the Lead Rapper, Vocalist and Maknae of the girl group GFriend.

Kim Ye-won (singer): Kim Ye-won (born December 5, 1989), also known mononymously as Yewon, is a South Korean actress, singer and entertainer.  She was debuted in 2011 as a member of K-pop girl group Jewelry.  Alongside her singing career, she appeared on television in dramas, sitcoms and variety shows.  After Jewelry disbanded in early 2015, Kim joined the fourth season of reality show "We Got Married", where she was paired with singer Henry Lau. It was confirmed that her contract with Star Empire Entertainment would be expired in the end of October 2016.  She later signed Jellyfish Entertainment in November 2016.

We Got Married (Season 4): "We Got Married" (Season 4) is the fourth season of South Korean MBC's "We Got Married" (), a reality variety show and was a segment of the "Sunday Sunday Night" program.  First broadcast in 2008, the show pairs up Korean celebrities to show what life would be like if they were married.  Each week, couples are assigned missions to complete, while interviews with the participants reveal their thoughts and feelings.

My House (TV series): My House () is a 2015 South Korean television program starring Lee Sang-min, Lee Ji-ae, Julian Quintart and Kim Ye-won.  It airs on JTBC on Tuesday at 0:30 beginning February 23, 2015.

Kim Ye-won (actress, born 1987): Kim Ye-won (born Kim Shin-ah on December 11, 1987) is a South Korean actress and singer.

Henry Lau: Henry Lau (born October 11, 1989), known mononymously as Henry, is a Canadian singer, rapper, dancer, composer, record producer, beatboxer, actor and entertainer mostly active in South Korea.  He debuted in 2008 as a member of Super Junior-M.  Aside from group activities, he has also produce several songs for various artists, television drama and also a part of a composing team NoizeBank.  He dubbed his fans as his Strings.

Bringing Up Bates: Bringing Up Bates is an American reality television show on Up TV.  It is centered around Gil and Kelly Jo Bates and their 19 children.  Gil and Kelly Jo got married on December 19, 1987, when he was 22 and she was 21.  Since then, they have had 9 boys and 10 girls, all of whom were born between the years 1988 and 2012, and Kelly Jo delivered every one of them.  There are no sets of multiples in their family either.  They have four children that are married: Zach (married Whitney Perkins), Michaella (married Brandon Keilen), Erin (married Chad Paine), and Alyssa (married John Webster).  Gil and Kelly Jo also have six grandchildren, two being Zach & Whitney's children, two being Chad & Erin's children, and the other two being John & Alyssa's children.  The Bates family had a TV show in 2012 called "United Bates of America", and it was announced in October 2014 that the Bates family would return in a new series which would be called "Bringing Up Bates".  The series debuted on January 1, 2015.  UP TV revealed that the show would be returning for another season in June 2015.  The second season started on June 4, 2015.  The third season started on January 7, 2016 The fourth season started on June 2, 2016.  The fifth season started on January 5, 2017.  The sixth season began on June 1, 2017.

Kim Ye-won (actress, born 1997): Kim Ye-won (born August 23, 1997) is a South Korean actress.

Question: What nationality is the singer who was paired with Kim Ye-won on the fourth season of We Got Married?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the reality show."
    },
    "season_number": {
      "type": "integer",
      "description": "The season number of the reality show."
    },
    "kim_ye_won_participant": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the participant Kim Ye-won."
        },
        "role_in_show": {
          "type": "string",
          "description": "Kim Ye-won's role in the show, e.g., participant."
        },
        "occupation_type": {
          "type": "string",
          "description": "The primary occupation type of this specific Kim Ye-won."
        }
      },
      "required": [
        "name",
        "role_in_show",
        "occupation_type"
      ],
      "additionalProperties": false
    },
    "paired_singer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the singer paired with Kim Ye-won."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the paired singer."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the paired singer."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "show_name",
    "season_number",
    "kim_ye_won_participant",
    "paired_singer"
  ],
  "additionalProperties": false
}

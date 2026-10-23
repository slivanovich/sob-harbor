{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNo Frauds: \"No Frauds\" is a song by Trinidadian rapper Nicki Minaj, with Canadian rapper Drake and American rapper Lil Wayne.  The song is a response to hip-hop artist Remy Ma’s \"Shether\" a 7 minute diss track aimed at Nicki Minaj.  Produced by Murda Beatz and Cubeatz, the song was released as a single on March 10, 2017 by Young Money Entertainment, Cash Money Records and Republic Records, along with \"Changed It\" and \"Regret in Your Tears\".  \"No Frauds\" sold 78,861 copies during the first week of its release debuting at #1 on R&B/Hip-Hop sales charts and #14 on the US \"Billboard\" Hot 100.\n\nBlack Friday (Lil' Kim mixtape): Black Friday is the second mixtape by American rapper Lil' Kim, released on February 14, 2011 through PayPal, for $7.99.  The title track is a response to Nicki Minaj's song \"Roman's Revenge\".  The mixtape also contains the track \"Grindin' Makin' Money\", a collaboration which features rappers Birdman and Nicki Minaj, which Kim claims ignited the feud between her and Minaj, as well as another diss song towards Minaj titled \"Pissin' on 'Em\".\n\nHot Spot (song): \"Hot Spot\" is the first single released from American female hip-hop artist Foxy Brown's second album \"Chyna Doll\".  It was released in the United States on October 26, 1998.  The single was produced by Murder Inc founder Irv Gotti and co-producer Lil' Rob, with lyrics written by Foxy Brown and hip-hop artist Jay-Z.  The single received a short-lived buzz and peaked at 91 on the Billboard Hot 100.  It was the last time Foxy Brown would make her appearance on the Billboard Hot 100 as a solo artist.\n\nChoice (rapper): Kim Davis, better known by her stage name of Choice or MC Choice, is an American female hip-hop artist based out of Houston, Texas.  She is best known for her album \"The Big Payback\", which first came out in 1990.  Signed to the label Rap-A-Lot Records, her strident, sexually explicit album prefigured the image and sound of later female rappers such as Lil' Kim, with music journalist Roni Sarig mentioning Choice in \"Third Coast: Outkast, Timbaland, and How Hip-Hop Became a Southern Thing\" as one of the U.S. south's underground kings and queens of rap alongside the Geto Boys and Street Military.\n\nPink Friday (fragrance): Pink Friday is the first fragrance created by Trinidadian rapper Nicki Minaj with Give Back Brands, first released on September 22, 2012 in the US and Australia.  The bottle was designed by Lance McGregor of Paul Meyers and Friends.  Elizabeth Arden bought the licence to distribute the fragrance to major retail stores worldwide.  With the success of \"Pink Friday\", Minaj released two limited edition flankers of the fragrance called \"\"Pink Friday Special Edition\"\", and \"\"Pink Friday Deluxe Edition\"\", respectively.  Minaj's \"Pink Friday\" perfume was nominated for three 2013 FiFi Awards for Fragrance of the Year, Best Packaging, and Media Campaign of the Year.  Pink Friday was succeeded by the fragrances \"Minajesty\" and \"Onika\".\n\nRemy Ma: Reminisce Mackie (née Smith; May 30, 1980), known professionally as Remy Ma, (formerly Remy Martin), is an American rapper.  She contributed to the songs \"Ante Up (Remix)\" (2001), \"Lean Back\" (2004), \"Conceited\" (2006) and \"All the Way Up\" (2016).  She is one of only five female rappers to ever top the \"Billboard\" charts and one of only three multiple winners of the BET Award for Best Female Hip-Hop Artist, which she won in 2005 and 2017.\n\nRoman Holiday (song): Roman Holiday is a song by Trinidadian hip hop artist Nicki Minaj, the opening track from her second album, \"\".  It was written by Nicki Minaj, Larry Nacht, Winston Thomas and Safarree Samuels, and produced by Blackout (Thomas) and Pink Friday Productions.  Two months prior to the album's official release, Minaj performed what many viewed as a controversial rendition of the song at the 54th Grammy Awards ceremony on February 12, 2012, which received generally unfavorable reviews from critics.  Reviewing the album, Jessica Hopper of \"Spin\" called the song itself \"pure theater, the closest hip-hop's gotten to its own Bohemian Rhapsody, full of thrilling crescendos and twitchy verses that verge on the ridiculous, but always shift toward the triumphant.\n\nLow (Juicy J song): \"Low\" is a song by American hip hop recording artist Juicy J.  It was released on August 7, 2014, intended as the first single from Juicy J's fourth studio album but faired poor commercially and was thereby removed from the project.  The song features guest appearances from American rappers, Lil Bibby, Young Thug and Nicki Minaj.  \"Low\" was written by Juicy J, Nicki Minaj, Lil Bibby, Dr. Luke, Rock City, and Cirkut, and it was produced by Dr. Luke and Cirkut.  The song received positive reception from music critics, most of it towards Nicki Minaj's appearance.  A music video directed by Benny Boom was created to promote the single.\n\nBET Award for Best Female Hip-Hop Artist: The BET Award for Best Female Hip-Hop Artist is an award given to honor the outstanding achievements female artists have made in Hip hop every year.  The winner is determined based on sales and overall quality of content released within the eligibility period.\n\nBET Awards 2013: The 2013 BET Awards were held at the Nokia Theatre L.A. Live in Los Angeles, California on June 30, 2013.  The awards ceremony recognized Americans in music, movies, sports and other fields of entertainment over the past year.  Chris Tucker hosted the event.  The BET Awards nominations were announced May 14, 2013 at a press conference on the rooftop of L.A.'s Icon Ultra Lounge, just up the street from the Nokia Theatre, where the BET Awards were staged for the first time.  Chris Brown was announced as the first confirmed performer.  Charlie Wilson was announced as this year's Cadillac Lifetime Achievement Award honoree.  R. Kelly also performed at the awards show.  The show was the culmination of the cable network's first ever BET Experience, a three-day music and lifestyle fest done in partnership with AEG Live.  Chris Brown won the Fandemonium Award for the fourth time in a row, while Nicki Minaj won Best Female Hip-Hop Artist, making history as the first female rapper to win the award four times consecutively.  The Young Stars award winner was awarded to Gabrielle Douglas, gold medalist in the 2012 London Summer Olympics.  The show opened with a performance by Chris Brown and Nicki Minaj performing Love More.\n\nQuestion: In 2017 Nicki Minaj released a response-track to which Best Female Hip-Hop Artist?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"responding_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who released the response track.\"\n    },\n    \"response_track_name\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the response track.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the response track was released.\"\n    },\n    \"target_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist who was the target of the response track.\"\n        },\n        \"award_won\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the award won by the target artist.\"\n        },\n        \"award_years\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"integer\"\n          },\n          \"description\": \"The years the target artist won the specified award.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"award_won\",\n        \"award_years\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"responding_artist_name\",\n    \"response_track_name\",\n    \"release_year\",\n    \"target_artist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "responding_artist_name": {
        "type": "string",
        "description": "The name of the artist who released the response track."
      },
      "response_track_name": {
        "type": "string",
        "description": "The title of the response track."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the response track was released."
      },
      "target_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist who was the target of the response track."
          },
          "award_won": {
            "type": "string",
            "description": "The name of the award won by the target artist."
          },
          "award_years": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "The years the target artist won the specified award."
          }
        },
        "required": [
          "name",
          "award_won",
          "award_years"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "responding_artist_name",
      "response_track_name",
      "release_year",
      "target_artist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

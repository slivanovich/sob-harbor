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
The X Factor (Australian TV series): The X Factor is an Australian television reality music competition, based on the original UK series, to find new singing talent.  The first season of the show premiered on Network Ten on 6 February 2005.  Ten dropped "The X Factor" after the first season due to poor ratings.  In 2010, the Seven Network won the rights to the show, and a second season went into production.  "The X Factor" was renewed after the highly successful "Australian Idol" was no longer broadcast on Network Ten.  "The X Factor" was produced by FremantleMedia Australia, and was broadcast on the Seven Network in Australia and on TV3 in New Zealand.  The program was cancelled after its eighth season in 2016.

Louis Walsh (disambiguation): Louis Walsh (born 1952) is an Irish entertainment manager and television personality.

X Factor Around the World: X Factor Around the World is the 24th anniversary television special of RCTI, joining four continents' biggest versions of "The X Factor" reality singing competition—"X Factor Indonesia" (Asia), "The X Factor USA" (America), "The X Factor UK" (Europe) and "The X Factor Australia" (Australia).  The show was originally aired on 24 August 2013 in Indonesia and featured performances by six winners and runners-up: Melanie Amaro, Samantha Jade, The Collective, Jahmene Douglas, Fatin Shidqia, Novita Dewi.

Eoghan Quigg: Eoghan Karl Christopher Quigg (pronounced "Owen", born 12 July 1992) is a pop singer from Dungiven, Northern Ireland, who finished third in the fifth series of the British television music talent contest "The X Factor" in 2008.  As a result of his "X Factor" success, Quigg was due to be signed by Simon Cowell, "X Factor" creator/producer and owner and CEO of Syco Records, but was instead signed to RCA after Cowell pulled out.  Quigg released an eponymous studio album in 2009, to strongly negative reviews.  Quigg competed in the Irish national selection for the chance to represent Ireland in 2014 at the Eurovision Song Contest but finished second.

The X Factor (Arabic TV series): The X Factor Arabia originally aired in March 26, 2006 with the title "XSeer Al Najah", meaning Elixir or Essence of Success.  "XSeer Al Najah" was the Arab version of "The X Factor".  The Arabic-language version of the program also created by Simon Cowell has a similar format to the British version, in that there are judges who each have a team of contestants to mentor and compete with each other for the X Factor title.  The 14-episode first series was broadcast in 22 Arabic-speaking countries.  In its debut, it was known as being one of the most watched programs on television and was produced and supported by Rotana, one of the largest production companies in the Arab World.  The winner of "XSeer Al Najah" earned a chance to sign with Rotana.

List of The X Factor finalists (UK series 8): The eighth UK series of "The X Factor" was broadcast on ITV from 20 August 2011, with the live shows starting on 8 October 2011.  Girl group Little Mix were the winners, and the runner-up was Marcus Collins.  After "The X Factor", several of the contestants went on to release singles, including Little Mix, Collins, Amelia Lily, Misha B, Frankie Cocozza, The Risk and 2 Shoes.  On 25 July 2013, three contestants from series 8 - Little Mix, Amelia Lily and Misha B - were included in the (three-minute 41-second) X Factor Ultimate Mash-Up, a video trailer for series 10, a selection of 13 tracks and artists chosen to represent a decade of 'The X Factor' artists impact on the UK national chart.

Louis Walsh: Michael Louis Vincent Walsh (born 5 August 1952) known as Louis Walsh is an Irish entertainment manager and judge on British television talent show "The X Factor".

Annastasia Baker: Annastasia Anneve Baker (born 16 November 1988) is a British Gospel singer, and song writer, Annastasia first caught the public eye as a contestant who progressed into the top six female singers in the judges round of the 2008 edition of The X Factor (UK series 5).  Undeterred by not getting past this stage, Annastasia subsequently auditioned for the X Factor 2010 series, The X Factor (UK series 7) and once again made it to the judges round.

The X Factor (UK series 1): The X Factor is a British television music competition to find new singing talent; the winner of which receives a £1 million recording contract with the Syco Music record label.  The first series was broadcast from 4 September to 11 December 2004.  The competition was split into several stages: auditions, bootcamp and live shows, with Louis Walsh, Sharon Osbourne and Simon Cowell as judges.  Kate Thornton presented the show on ITV, whilst Ben Shephard presented spin-off show "The Xtra Factor" on ITV2.

X Factor (Albanian TV series): X Factor Albania is the Albanian version of "The X Factor", adapted from the original UK series to find new singing talent.  The first season started in January 8, 2012, and it is broadcast by TV Klan.  The judges are: Albanian singer from Macedonia Altuna Sejdiu, Albanian singer Soni Malaj, Albanian superstar Alban Skënderaj, and the famous composer Pandi Laço.  The show is hosted by Alketa Vejsiu.  She applied to acquire the rights of the show along with Top Channel and TV Klan.  Syco TV gave the rights to her, then she sold parts of the rights to TV Klan.  After losing the rights of "The X Factor", Top Channel acquired the rights of the talent show, "The Voice".

Question: Which of the judges of The X Factor is an Irish entertainment manager?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "judge_name": {
      "type": "string",
      "description": "The name of the judge."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the judge."
    },
    "primary_profession": {
      "type": "string",
      "description": "The primary profession of the judge as described in the context."
    },
    "judged_show_details": {
      "type": "array",
      "description": "Details about the X Factor series the person judged.",
      "items": {
        "type": "object",
        "properties": {
          "show_title": {
            "type": "string",
            "description": "The title of The X Factor series."
          },
          "role": {
            "type": "string",
            "description": "The role of the person on the show."
          },
          "series_identifier": {
            "type": "string",
            "description": "A specific identifier for the series (e.g., 'UK series 1')."
          }
        },
        "required": [
          "show_title",
          "role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "judge_name",
    "nationality",
    "primary_profession",
    "judged_show_details"
  ],
  "additionalProperties": false
}

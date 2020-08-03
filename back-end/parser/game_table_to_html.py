from datetime import datetime


def game_table_to_html(game_table, game_headline):
    """
    Format the <game_table> for the Game.
    """
    game_table.sort_values("SCORE", ascending=False, ignore_index=True, inplace=True)
    html = game_table.to_html(escape=False, border=0, index=False)
    html = html.replace('<table border="0" class="dataframe"', '<table class="leaderboard"')
    html = html.replace('<tr style="text-align: right;">', '<tr>')

    new_html = []
    if game_headline == "LEADERBOARD":
        new_html.append('<h1><strong>LEADERBOARD &#127798;</strong></h1>')
    else:
        new_html.append('<h2 style="text-align: center; color: rgb(206,17,65);"><strong>' +
                        game_headline + '</strong></h2>')

    # set colours for top 3 and heading and ending
    td_count = 0
    for line in html.splitlines():
        if '<td>' in line:
            td_count += 1

            # gold
            if td_count == 1:
                line = line.replace('<a', '<a style="color:rgb(214,175,54)"')

            # silver leader-board
            if td_count == 3 and game_headline == "LEADERBOARD":
                line = line.replace('<a', '<a style="color:rgb(167,167,173)"')

            # silver game
            if td_count == 4 and game_headline != "LEADERBOARD":
                line = line.replace('<a', '<a style="color:rgb(167,167,173)"')

            # bronze leader-board
            if td_count == 5 and game_headline == "LEADERBOARD":
                line = line.replace('<a', '<a style="color:rgb(167,112,68)"')

            # bronze game
            if td_count == 7 and game_headline != "LEADERBOARD":
                line = line.replace('<a', '<a style="color:rgb(167,112,68)"')

        new_html.append(line)

    current_time = datetime.today().strftime('<p style="text-align: center; padding-left: 0%; padding-right: 0%;\
    font-size: smaller;">Updated: %B %d, %Y at %X - ET</p>')
    new_html.append(current_time)
    new_html.append('<br>')

    new_html = "\n".join(new_html)
    return new_html

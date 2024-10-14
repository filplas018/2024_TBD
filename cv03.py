"""
Vizualizace dat z webu iDNES.cz

Tento skript využívá data získaná z webu iDNES.cz a nabízí několik vizualizací, které poskytují pohled na různé aspekty článků.

Vizualizace zahrnují:
1. Časovou křivku přidávání článků: Zobrazuje, jak se počet publikovaných článků měnil v průběhu času.
2. Sloupcový graf počtu článků podle roků: Ukazuje počet článků vydaných v jednotlivých rocích.
3. Scatter plot délky článku a počtu komentářů: Zobrazuje vztah mezi délkou článku a počtem komentářů, což umožňuje analyzovat, zda delší články přitahují více komentářů.
4. Koláčový graf podílu článků v kategoriích: Vizualizuje podíly článků napříč různými kategoriemi, což poskytuje přehled o rozložení obsahu.
5. Histogram počtu slov v článcích: Ukazuje distribuci počtu slov v článcích a poskytuje přehled o průměrné délce článků.
6. Histogram délky slov v článcích: Vizualizuje průměrnou délku slov v článcích a distribuci délek slov.
7. Časová analýza výskytu klíčových slov "koronavirus" a "vakcína" v názvech článků: Ukazuje, jak často se tato klíčová slova objevovala v průběhu času, což může reflektovat trendy zájmu.
8. Histogram počtu článků podle dnů v týdnu: Analyzuje, v které dny týdne je publikováno nejvíce článků.

Použité knihovny pro vizualizaci:
- Můžete zvolit knihovnu dle vlastních preferencí. Mezi doporučené patří matplotlib, Seaborn, Plotly nebo ggplot.

Před spuštěním skriptu se ujistěte, že máte nainstalované všechny potřebné knihovny pro práci s daty a tvorbu grafů.
"""
# Omi Dfdl Definitions

Omi Dfdl definitions provide declarative, cross language parsing of common binary exchange protocols.

For more information on Dfdl: [Dfdl](https://daffodil.apache.org/docs/dfdl/ "Data Format Description Language")

[![Apache Daffodil](https://github.com/Open-Markets-Initiative/Directory/blob/main/About/Images/Daffodil.png)](https://daffodil.apache.org/)

These definitions are built and tested with the DFDL reference implementation: [Apache Daffodil](https://daffodil.apache.org/ "Apache Daffodil")
## Usage

Each .dfdl.xsd file is a complete declarative description of one protocol version, expressed as a DFDL annotated XML schema. Compile a schema into a saved parser with the Apache Daffodil reference processor:

```
daffodil save-parser -s Iex/IexEquities_Tops_v1_6_6.dfdl.xsd -r packet tops.parser
```
A saved parser turns wire bytes into XML, JSON, or an infoset for any Daffodil host language, including Java, Scala, and C.

For processor information: [Apache Daffodil](https://daffodil.apache.org/releases/ "Apache Daffodil Releases")
## Development

Updates are greatly appreciated; however, this entire repository is source generated...including the words you are reading right now. If you wish to suggest definition updates, the recommended process is to create an issue with changes and explanation.  Time permitting, we will update the models and regenerate.

| Protocol Count | Generated Lines |
| --- | --- |
| 115 | 220,301 |

## Testing

[![Build](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/actions/workflows/build.yml/badge.svg)](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/actions/workflows/build.yml)

Please report any parsing errors as an [issue](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/issues "Omi Dfdl Issues").  Include a small note on the protocol and version, and a minimal capture demonstrating the problem. Also consider including a link or pdf specification documenting the correct behavior.

Production packet captures are required for protocol verification.  If your organization has the rights to packet captures, and you wish to make the world a better place, please post captures to this project.

## Open Markets Initiative

[![Omi](https://github.com/Open-Markets-Initiative/Directory/blob/main/About/Images/Logo.png)](https://github.com/Open-Markets-Initiative/Directory)  The Open Markets Initiative (Omi) is a group of technologists dedicated to enhancing the stability of electronic financial markets using modern development methods.

For a list of Omi Hft projects: [Omi Projects](https://github.com/Open-Markets-Initiative/Directory/tree/main/Projects "Open Markets Initiative Projects")

For details of Omi rules and regulations: [Omi Directory](https://github.com/Open-Markets-Initiative/Directory "Open Markets Initiative Directory")
## Organizations

> [Cme][Cme.Directory] · [Coinbase][Coinbase.Directory] · [Iex][Iex.Directory] · [Nasdaq][Nasdaq.Directory]

## Exchanges, Ats, and Sips

> [CoinbaseDerivatives][CoinbaseDerivatives.Exchange] · [Deribit][Deribit.Exchange] · [GemxOptions][GemxOptions.Exchange] · [IexEquities][IexEquities.Exchange] · [IexOptions][IexOptions.Exchange] · [IseOptions][IseOptions.Exchange] · [MrxOptions][MrxOptions.Exchange] · [NomOptions][NomOptions.Exchange] · [NsmEquities][NsmEquities.Exchange] · [NtxEquities][NtxEquities.Exchange] · [NtxOptions][NtxOptions.Exchange] · [PhlxOptions][PhlxOptions.Exchange] · [PsxEquities][PsxEquities.Exchange] · [Uqdf][Uqdf.Consolidator] · [Utdf][Utdf.Consolidator] · [Utp][Utp.Consolidator]

## Disclaimer

Any similarities between existing people, places and/or protocols is purely incidental.

Enjoy.

[Omi Projects]: https://github.com/Open-Markets-Initiative/Directory/tree/main/Projects "Open Markets Initiative Projects"
[Omi Rules and Regulations]: https://github.com/Open-Markets-Initiative/Directory/tree/main/License "Open Markets Initiative Rules and Regulations"

[Omi.Glossary.Testing]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Protocol Testing Status"
[Omi.Glossary.Testing.Verified]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Testing Status: Protocol has been tested on live data"
[Omi.Glossary.Testing.Incomplete]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Testing Status: Protocol has been tested on live data but contains known issues"
[Omi.Glossary.Testing.Beta]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Testing Status: Protocol has not been tested and structure is speculative"
[Omi.Glossary.Testing.Untested]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Testing Status: Protocol has not been tested on live data"
[Omi.Encoding.Definitions]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/ReadMe.md "Encoding Directory"

[Omi.Encoding.Sbe]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Sbe.md "Sbe Encoding"
[Omi.Encoding.Tcp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Tcp.md "Tcp Encoding"
[Omi.Encoding.IexTp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/IexTp.md "IexTp Encoding"
[Omi.Encoding.Itch]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Itch.md "Itch Encoding"
[Omi.Encoding.Ouch]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Ouch.md "Ouch Encoding"
[Omi.Encoding.Utp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Utp.md "Utp Encoding"

[Cme.Globex.Mdp3]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/Mdp3.md "Market Data Platform 3"
[Cme.Globex.Streamlined]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/Streamlined.md "Streamlined Market Data"
[Cme.Globex.Settlements]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/Settlements.md "Settlements"
[Cme.Globex.Derived]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/Derived.md "Derived Market Data"
[Cme.Globex.EbsSpectrum]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/EbsSpectrum.md "Ebs Spectrum Market Data"
[Cme.Globex.BrokerTecUst]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/BrokerTecUst.md "BrokerTec Us Treasuries"
[Cme.Globex.iLink3]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Cme/Protocols/Globex/iLink3.md "iLink 3"
[Coinbase.CoinbaseDerivatives.MarketDataApi]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Coinbase/Protocols/CoinbaseDerivatives/MarketDataApi.md "Market Data Api"
[Coinbase.CoinbaseDerivatives.OrdersApi]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Coinbase/Protocols/CoinbaseDerivatives/OrdersApi.md "Orders Api"
[Coinbase.CoinbaseDerivatives.Session]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Coinbase/Protocols/CoinbaseDerivatives/Session.md "Session Layer"
[Coinbase.Deribit.MarketDataApi]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Coinbase/Protocols/Deribit/MarketDataApi.md "Market Data Api"
[Coinbase.Deribit.OrdersApi]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Coinbase/Protocols/Deribit/OrdersApi.md "Orders Api"
[Iex.IexEquities.Tops]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/Tops.md "Top Of Book"
[Iex.IexEquities.Deep]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/Deep.md "Depth Of Book"
[Iex.IexEquities.DeepPlus]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/DeepPlus.md "DeepPlus"
[Iex.IexOptions.MarketData]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexOptions/MarketData.md "Market Data"
[Iex.IexOptions.BinaryOrderEntry]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexOptions/BinaryOrderEntry.md "Binary Order Entry"
[Nasdaq.GemxOptions.DepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/GemxOptions/DepthOfMarket.md "Depth Of Market"
[Nasdaq.GemxOptions.OrderFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/GemxOptions/OrderFeed.md "Order Feed"
[Nasdaq.GemxOptions.TopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/GemxOptions/TopOfMarket.md "Top Of Market"
[Nasdaq.GemxOptions.TradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/GemxOptions/TradeFeed.md "Trade Feed"
[Nasdaq.IseOptions.OrderComboFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/OrderComboFeed.md "Ise Order Combo Market Data Feed"
[Nasdaq.IseOptions.OrderFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/OrderFeed.md "Ise Order Feed Market Data"
[Nasdaq.IseOptions.TopComboQuoteFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/TopComboQuoteFeed.md "Ise Top Combo Quote Feed"
[Nasdaq.IseOptions.DepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/DepthOfMarket.md "Depth Of Market"
[Nasdaq.IseOptions.SpreadDepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/SpreadDepthOfMarket.md "Phlx Options Spread Depth"
[Nasdaq.IseOptions.SpreadOrders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/SpreadOrders.md "Phlx Options Spread Orders"
[Nasdaq.IseOptions.SpreadTopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/SpreadTopOfMarket.md "Phlx Options Spread Top Of Market"
[Nasdaq.IseOptions.SpreadTradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/SpreadTradeFeed.md "Phlx Options Spread Trade Feed"
[Nasdaq.IseOptions.TopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/TopOfMarket.md "Top Of Market"
[Nasdaq.IseOptions.TradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/IseOptions/TradeFeed.md "Trade Feed"
[Nasdaq.MrxOptions.DepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/DepthOfMarket.md "Depth Of Market"
[Nasdaq.MrxOptions.OrderFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/OrderFeed.md "Order Feed"
[Nasdaq.MrxOptions.SpreadDepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/SpreadDepthOfMarket.md "Phlx Options Spread Depth"
[Nasdaq.MrxOptions.SpreadOrders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/SpreadOrders.md "Phlx Options Spread Orders"
[Nasdaq.MrxOptions.SpreadTopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/SpreadTopOfMarket.md "Phlx Options Spread Top Of Market"
[Nasdaq.MrxOptions.SpreadTradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/SpreadTradeFeed.md "Phlx Options Spread Trade Feed"
[Nasdaq.MrxOptions.TopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/TopOfMarket.md "Top Of Market"
[Nasdaq.MrxOptions.TradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/MrxOptions/TradeFeed.md "Trade Feed"
[Nasdaq.NomOptions.Bono]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NomOptions/Bono.md "Nom Binary Order Entry"
[Nasdaq.NomOptions.Itto]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NomOptions/Itto.md "Itch To Trade Options"
[Nasdaq.NtxEquities.TotalView]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NtxEquities/TotalView.md "TX TotalView Itch"
[Nasdaq.NtxEquities.Orders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NtxEquities/Orders.md "BX Orders"
[Nasdaq.NtxOptions.TopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NtxOptions/TopOfMarket.md "Top Of Market"
[Nasdaq.NtxOptions.TradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NtxOptions/TradeFeed.md "Trade Feed"
[Nasdaq.NtxOptions.DepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NtxOptions/DepthOfMarket.md "Depth Of Market"
[Nasdaq.PhlxOptions.DepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/DepthOfMarket.md "Depth Of Market"
[Nasdaq.PhlxOptions.Orders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/Orders.md "PHLX Orders"
[Nasdaq.PhlxOptions.Topo]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/Topo.md "Phlx Top Order Market Data"
[Nasdaq.PhlxOptions.SpreadDepthOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/SpreadDepthOfMarket.md "Spread Depth"
[Nasdaq.PhlxOptions.SpreadOrders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/SpreadOrders.md "Spread Orders"
[Nasdaq.PhlxOptions.SpreadTopOfMarket]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/SpreadTopOfMarket.md "Spread Top Of Market"
[Nasdaq.PhlxOptions.SpreadTradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/SpreadTradeFeed.md "Spread Trade Feed"
[Nasdaq.PhlxOptions.TradeFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PhlxOptions/TradeFeed.md "Trade Feed"
[Nasdaq.PsxEquities.LastSale]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PsxEquities/LastSale.md "Last Sale"
[Nasdaq.PsxEquities.TotalView]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PsxEquities/TotalView.md "TotalView Itch"
[Nasdaq.PsxEquities.Bbo]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PsxEquities/Bbo.md "Best Bid And Offer"
[Nasdaq.PsxEquities.Orders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/PsxEquities/Orders.md "Orders"
[Nasdaq.NsmEquities.Aggregated]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/Aggregated.md "TotalView Aggregated"
[Nasdaq.NsmEquities.Level2]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/Level2.md "Level 2"
[Nasdaq.NsmEquities.NlsPlus]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/NlsPlus.md "Last Sale Plus"
[Nasdaq.NsmEquities.Nois]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/Nois.md "Net Order Imbalance Snapshot"
[Nasdaq.NsmEquities.NoiView]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/NoiView.md "Net Order Imbalance View"
[Nasdaq.NsmEquities.Orders]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/Orders.md "Orders"
[Nasdaq.NsmEquities.TotalView]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/NsmEquities/TotalView.md "TotalView Itch"
[Nasdaq.Uqdf.Output]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/Uqdf/Output.md "Output"
[Nasdaq.Utdf.Output]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/Utdf/Output.md "Output"
[Nasdaq.Utp.Input]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/Utp/Input.md ""
[Nasdaq.Utp.Snapshot]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Nasdaq/Protocols/Utp/Snapshot.md "Snapshot"

[Cme.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/cme "CME Group"
[Coinbase.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/coinbase "Coinbase"
[Iex.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/iex "Investors Exchange"
[Nasdaq.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq "National Association of Securities Dealers Automated Quotations (Nasdaq)"

[CoinbaseDerivatives.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/coinbase/coinbasederivatives "Coinbase Derivatives"
[Deribit.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/coinbase/deribit "Deribit"
[GemxOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/gemxoptions "Nasdaq GEMX"
[Globex.Platform]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/cme "CME Globex"
[IexEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/iex/iexequities "IEX Equities"
[IexOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/iex/iexoptions "IEX Options"
[IseOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/iseoptions "Nasdaq ISE"
[MrxOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/mrxoptions "Nasdaq MRX"
[NomOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/nomoptions "Nasdaq Options Market"
[NsmEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/nsmequities "Nasdaq Stock Market"
[NtxEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/ntxequities "Nasdaq Texas"
[NtxOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/ntxoptions "Nasdaq Texas Options"
[PhlxOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/phlxoptions "Nasdaq PHLX"
[PsxEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/psxequities "Nasdaq PSX"
[Uqdf.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/uqdf "Nasdaq UTP Quote Data Feed"
[Utdf.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/utdf "Nasdaq UTP Trade Data Feed"
[Utp.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/utp "Nasdaq Unlisted Trading Privileges Plan"

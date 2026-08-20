# Omi DFDL Definitions

Omi Data Format Description Language ([DFDL](https://en.wikipedia.org/wiki/Data_Format_Description_Language "Data Format Description Language")) definitions provide declarative, cross language parsing of common binary exchange protocols.


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
| 314 | 2,929,792 |

## Testing

[![Build](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/actions/workflows/build.yml/badge.svg)](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/actions/workflows/build.yml)

Please report any parsing errors as an [issue](https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/issues "Omi Dfdl Issues").  Include a small note on the protocol and version, and a minimal capture demonstrating the problem. Also consider including a link or pdf specification documenting the correct behavior.

Production packet captures are required for protocol verification.  If your organization has the rights to packet captures, and you wish to make the world a better place, please post captures to this project.

## Open Markets Initiative

[![Omi](https://github.com/Open-Markets-Initiative/Directory/blob/main/About/Images/Logo.png)](https://github.com/Open-Markets-Initiative/Directory)  The Open Markets Initiative (Omi) is a group of technologists dedicated to enhancing the stability of electronic financial markets using modern development methods.

For a list of Omi Hft projects: [Omi Projects](https://github.com/Open-Markets-Initiative/Directory/tree/main/Projects "Open Markets Initiative Projects")

For details of Omi rules and regulations: [Omi Directory](https://github.com/Open-Markets-Initiative/Directory "Open Markets Initiative Directory")
## Organizations

> [24X][24X.Directory] · [A2X][A2X.Directory] · [Aquis][Aquis.Directory] · [Asx][Asx.Directory] · [B3][B3.Directory] · [Bist][Bist.Directory] · [BlueOceanAts][BlueOceanAts.Directory] · [Cme][Cme.Directory] · [Coinbase][Coinbase.Directory] · [Eurex][Eurex.Directory] · [Euronext][Euronext.Directory] · [Iex][Iex.Directory] · [Nasdaq][Nasdaq.Directory]

## Exchanges

> [24XEquities][24XEquities.Exchange] · [AquisEquities][AquisEquities.Exchange] · [AsxDerivatives][AsxDerivatives.Exchange] · [AsxSecurities][AsxSecurities.Exchange] · [B3Derivatives][B3Derivatives.Exchange] · [BorsaIstanbul][BorsaIstanbul.Exchange] · [CoinbaseDerivatives][CoinbaseDerivatives.Exchange] · [Deribit][Deribit.Exchange] · [GemxOptions][GemxOptions.Exchange] · [IexEquities][IexEquities.Exchange] · [IexOptions][IexOptions.Exchange] · [IseOptions][IseOptions.Exchange] · [MrxOptions][MrxOptions.Exchange] · [NomOptions][NomOptions.Exchange] · [NsmEquities][NsmEquities.Exchange] · [NtxEquities][NtxEquities.Exchange] · [NtxOptions][NtxOptions.Exchange] · [PhlxOptions][PhlxOptions.Exchange] · [PsxEquities][PsxEquities.Exchange] · [BlueEquities][BlueEquities.Ats]

## Platforms

> [Cme Globex][Globex.Platform] · [Euronext Optiq][Optiq.Platform] · [Eurex T7][T7.Platform]

## Consolidators

> [Uqdf][Uqdf.Consolidator] · [Utdf][Utdf.Consolidator] · [Utp][Utp.Consolidator]

## Related Definitions

The Open Markets Initiative provides protocol definitions in several formats:

- [Kaitai Struct Definitions][Kaitai.Definitions.Repository] — cross language binary parsers with the kaitai struct compiler
- [P4 Definitions][P4.Definitions.Repository] — P4 programs for software and hardware data planes
- [Spicy Definitions][Spicy.Definitions.Repository] — declarative Spicy grammars for the zeek network security monitor
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
[Omi.Glossary.Testing.Unavailable]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Glossary/Testing.md "Testing Status: Protocol does not state a testing status"
[Omi.Encoding.Definitions]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/ReadMe.md "Encoding Directory"

[Omi.Encoding.Sbe]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Sbe.md "Sbe Encoding"
[Omi.Encoding.Amd]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Amd.md "Amd Encoding"
[Omi.Encoding.Atp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Atp.md "Atp Encoding"
[Omi.Encoding.Itch]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Itch.md "Itch Encoding"
[Omi.Encoding.Ouch]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Ouch.md "Ouch Encoding"
[Omi.Encoding.Udp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Udp.md "Udp Encoding"
[Omi.Encoding.Tcp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Tcp.md "Tcp Encoding"
[Omi.Encoding.Fbe]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Fbe.md "Fbe Encoding"
[Omi.Encoding.IexTp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/IexTp.md "IexTp Encoding"
[Omi.Encoding.Snap]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Snap.md "Snap Encoding"
[Omi.Encoding.Utp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Protocols/Utp.md "Utp Encoding"

[24X.24XEquities.Memo]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/24X/Protocols/24XEquities/Memo.md "Members Orders"
[24X.24XEquities.MemoirDepthFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/24X/Protocols/24XEquities/MemoirDepthFeed.md "Member Order Information Record Depth Feed"
[24X.24XEquities.MemoirLastSale]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/24X/Protocols/24XEquities/MemoirLastSale.md "Member Order Information Record Last Sale"
[24X.24XEquities.MemoirTopOfBook]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/24X/Protocols/24XEquities/MemoirTopOfBook.md "Member Order Information Record Top Of Book"
[A2X.A2XEquities.Rtmdf]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/A2X/Protocols/A2XEquities/Rtmdf.md "Real Time Market Data Feed"
[A2X.A2XEquities.Snapshot]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/A2X/Protocols/A2XEquities/Snapshot.md "Snapshot Feed"
[A2X.A2XEquities.UdpHeader]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/A2X/Protocols/A2XEquities/UdpHeader.md "Udp Headers"
[Aquis.AquisEquities.RealTime]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/RealTime.md "Real Time Market Data Feed"
[Aquis.AquisEquities.Replay]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/Replay.md "Market Data Replay"
[Aquis.AquisEquities.Snapshot]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/Snapshot.md "Aquis Market Data Snapshot"
[Aquis.AquisEquities.UdpHeader]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/UdpHeader.md "Udp Headers"
[Aquis.AquisEquities.TcpHeader]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/TcpHeader.md "Tcp Headers"
[Aquis.AquisEquities.TradingProtocol]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Aquis/Protocols/AquisEquities/TradingProtocol.md "Aquis Trading Protocol"
[Asx.AsxDerivatives.Ntp]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Asx/Protocols/AsxDerivatives/Ntp.md "New Trading Platform"
[Asx.AsxDerivatives.T24]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Asx/Protocols/AsxDerivatives/T24.md "24 Itch"
[Asx.AsxSecurities.Trade]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Asx/Protocols/AsxSecurities/Trade.md "Asx Trade"
[B3.B3Derivatives.BinaryUmdf]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/B3/Protocols/B3Derivatives/BinaryUmdf.md "Binary Unified Market Data Feed"
[B3.B3Derivatives.BinaryEntryPoint]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/B3/Protocols/B3Derivatives/BinaryEntryPoint.md "Binary Entry Point"
[Bist.BorsaIstanbul.GeniumInet]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Bist/Protocols/BorsaIstanbul/GeniumInet.md "Genium Inet"
[BlueOceanAts.BlueEquities.MemoirDepthFeed]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/BlueOceanAts/Protocols/BlueEquities/MemoirDepthFeed.md "Member Order Information Record Depth Feed"
[BlueOceanAts.BlueEquities.MemoirLastSale]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/BlueOceanAts/Protocols/BlueEquities/MemoirLastSale.md "Member Order Information Record Last Sale"
[BlueOceanAts.BlueEquities.MemoirTopOfBook]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/BlueOceanAts/Protocols/BlueEquities/MemoirTopOfBook.md "Member Order Information Record Top Of Book"
[BlueOceanAts.CommonHeader]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/BlueOceanAts/Protocols/CommonHeader.md "Common Header"
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
[Eurex.T7.Eobi]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Eurex/Protocols/T7/Eobi.md "Enhanced Order Book Interface"
[Eurex.T7.Eti]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Eurex/Protocols/T7/Eti.md "Enhanced Trading Interface"
[Eurex.T7.Xti]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Eurex/Protocols/T7/Xti.md "Cash Enhanced Trading Interface"
[Eurex.T7.Edci]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Eurex/Protocols/T7/Edci.md "Extended Derivatives Clearing Interface"
[Euronext.Optiq.MarketDataGateway]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Euronext/Protocols/Optiq/MarketDataGateway.md "Market Data Gateway"
[Euronext.Optiq.OrderEntryGateway]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Euronext/Protocols/Optiq/OrderEntryGateway.md "Order Entry Gateway"
[Euronext.Optiq.DropCopyGateway]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Euronext/Protocols/Optiq/DropCopyGateway.md "Drop Copy Gateway"
[Iex.IexEquities.Tops]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/Tops.md "Top Of Book"
[Iex.IexEquities.Deep]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/Deep.md "Depth Of Book"
[Iex.IexEquities.DeepPlus]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/DeepPlus.md "DeepPlus"
[Iex.IexEquities.IexTpHeader]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexEquities/IexTpHeader.md "IexTp Header"
[Iex.IexOptions.MarketData]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexOptions/MarketData.md "Market Data"
[Iex.IexOptions.BinaryOrderEntry]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexOptions/BinaryOrderEntry.md "Binary Order Entry"
[Iex.IexOptions.Session]: https://github.com/Open-Markets-Initiative/Directory/blob/main/Organizations/Iex/Protocols/IexOptions/Session.md "Session"
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

[24X.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/24x "24 National Exchange"
[A2X.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/a2x "A2X Markets"
[Aquis.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/aquis "Aquis Exchange"
[Asx.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/asx "Australian Securities Exchange"
[B3.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/b3 "Brasil, Bolsa, Balcão"
[Bist.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/bist "Borsa İstanbul A.Ş."
[BlueOceanAts.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/blueoceanats "Blue Ocean Technologies"
[Cme.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/cme "CME Group"
[Coinbase.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/coinbase "Coinbase"
[Eurex.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/eurex "Eurex Exchange"
[Euronext.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/euronext "Euronext"
[Iex.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/iex "Investors Exchange"
[Nasdaq.Directory]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq "National Association of Securities Dealers Automated Quotations (Nasdaq)"

[24XEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/24x "24X Equities"
[AquisEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/aquis "Aquis Equities"
[AsxDerivatives.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/asx/asxderivatives "Asx Derivatives"
[AsxSecurities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/asx/asxsecurities "Asx Securities"
[B3Derivatives.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/b3 "B3 Derivatives"
[BlueEquities.Ats]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/blueoceanats/blueequities "Blue Equities"
[BorsaIstanbul.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/bist "Borsa Istanbul"
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
[Optiq.Platform]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/euronext "Euronext Optiq"
[PhlxOptions.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/phlxoptions "Nasdaq PHLX"
[PsxEquities.Exchange]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/psxequities "Nasdaq PSX"
[T7.Platform]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/eurex "T7"
[Uqdf.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/uqdf "Nasdaq UTP Quote Data Feed"
[Utdf.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/utdf "Nasdaq UTP Trade Data Feed"
[Utp.Consolidator]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions/tree/main/nasdaq/utp "Nasdaq Unlisted Trading Privileges Plan"

[Kaitai.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-kaitai-struct-definitions "Omi Kaitai Struct Definitions"
[P4.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-p4-definitions "Omi P4 Definitions"
[Spicy.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-spicy-definitions "Omi Spicy Definitions"

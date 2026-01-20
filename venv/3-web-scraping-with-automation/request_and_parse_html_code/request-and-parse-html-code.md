# request-and-parse-html-code

After you've inspected your data source, the next step is to create a request to the website that you want to scrape data from, and then parse the response you get back.

**_SUMMARY_**

1. Discover code writing.
2. Create requests.
3. Parse HTML.

In this lesson, you'll discover how to write code to successfully create a request and parse HTML code. Your first goal is to create a request to get HTML code from this webpage, which contains a public catalog of books that are in English and categorized as humorous.

Copy this URL and then open up request and parse starter code.py in VS Code. At the top, the libraries you'll need have been imported. Requests and BeautifulSoup. Paste in the URL and store it in a variable as a string.

Call `requests.get` func, pass in the URL, and the header's argument equal to a dictionary that maps accept to text slash html. This ensures that you will only get HTML in the response. Save the result in a variable called response. Your second goal is to parse the HTML response. So call BeautifulSoup and pass in response.text followed by HTML.parser. This second argument tells BeautifulSoup to use Python's builtin HTML parser. Save the result in a variable named parsed response.

Finally, call parsed response.prettify to format the parsed HTML response in a way that's easier to read and print it out. Now save the program and run it. As you can see, the program successfully got HTML code from the webpage. Go ahead and practice with a webpage of your own. Make a request to get HTML content from the webpage using the request library and then parse it using the BeautifulSoup library.

## The Code

The import statements that bring in external Python libraries:

`import requests`
This imports the `requests` library, which is used to make HTTP requests (like GET and POST) to websites. In this code, it's used to fetch the HTML content from the URL.

`from bs4 import BeautifulSoup`
This imports the BeautifulSoup class from the bs4 (Beautiful Soup 4) library. BeautifulSoup is a web scraping tool that parses HTML and XML documents, making it easy to navigate and extract data from web pages.

Together, these libraries enable the script to download a webpage (`requests`) and then parse its HTML structure (`BeautifulSoup`) so you can extract specific information from it.

Line 41 will ensure we only get HTML in the response.
Line 48: Call BeautifulSoup. The second argument tells BeautifulSoup to use Python's builtin HTML parser.

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks"

# send a request to get html code from that url
response = requests.get(url, headers={"Accept": "text/html"})

# parse the response
parsed_response = BeautifulSoup(response.text, "html.parser")

# format the parsed HTML response in a way that’s easier to read and print it out
print(parsed_response.prettify())
```

### Testing

Run the program: `python3 request_and_parse.py`

### Results

In the Terminal, I've successfully got HTML content from the webpage.

```html
(using-python-for-automation-1) Mac:request_and_parse_html_code vanessatsanguk$
python3 request_and_parse.py
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <title>Just a moment...</title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="IE=Edge" http-equiv="X-UA-Compatible" />
    <meta content="noindex,nofollow" name="robots" />
    <meta content="width=device-width,initial-scale=1" name="viewport" />
    <style>
      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      html {
        line-height: 1.15;
        -webkit-text-size-adjust: 100%;
        color: #313131;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
          'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji',
          'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
      }
      body {
        display: flex;
        flex-direction: column;
        height: 100vh;
        min-height: 100vh;
      }
      .main-content {
        margin: 8rem auto;
        padding-left: 1.5rem;
        max-width: 60rem;
      }
      @media (width <= 720px) {
        .main-content {
          margin-top: 4rem;
        }
      }
      .h2 {
        line-height: 2.25rem;
        font-size: 1.5rem;
        font-weight: 500;
      }
      @media (width <= 720px) {
        .h2 {
          line-height: 1.5rem;
          font-size: 1.25rem;
        }
      }
      #challenge-error-text {
        background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0IyMEYwMyIgZD0iTTE2IDNhMTMgMTMgMCAxIDAgMTMgMTNBMTMuMDE1IDEzLjAxNSAwIDAgMCAxNiAzbTAgMjRhMTEgMTEgMCAxIDEgMTEtMTEgMTEuMDEgMTEuMDEgMCAwIDEtMTEgMTEiLz48cGF0aCBmaWxsPSIjQjIwRjAzIiBkPSJNMTcuMDM4IDE4LjYxNUgxNC44N0wxNC41NjMgOS41aDIuNzgzem0tMS4wODQgMS40MjdxLjY2IDAgMS4wNTcuMzg4LjQwNy4zODkuNDA3Ljk5NCAwIC41OTYtLjQwNy45ODQtLjM5Ny4zOS0xLjA1Ny4zODktLjY1IDAtMS4wNTYtLjM4OS0uMzk4LS4zODktLjM5OC0uOTg0IDAtLjU5Ny4zOTgtLjk4NS40MDYtLjM5NyAxLjA1Ni0uMzk3Ii8+PC9zdmc+');
        background-repeat: no-repeat;
        background-size: contain;
        padding-left: 34px;
      }
      @media (prefers-color-scheme: dark) {
        body {
          background-color: #222;
          color: #d9d9d9;
        }
      }
    </style>
    <meta content="360" http-equiv="refresh" />
  </head>
  <body>
    <div class="main-wrapper" role="main">
      <div class="main-content">
        <noscript>
          <div class="h2">
            <span id="challenge-error-text">
              Enable JavaScript and cookies to continue
            </span>
          </div>
        </noscript>
      </div>
    </div>
    <script>
      (function () {
        window._cf_chl_opt = {
          cvId: '3',
          cZone: 'www.feedbooks.com',
          cType: 'managed',
          cRay: '9c020dc7cece3e7e',
          cH: 'fC97Bi7uwLUnkm5P5ihu79UTJ5V5hyVMe1pL8NXRyJs-1768780847-1.2.1.1-M7N8eAP6kvWXsclZO8Etrf1T5iA09oghYgB5hTsMTG5YmBd79c0PpxWMDomFMDmu',
          cUPMDTk:
            '\/search?cat=FBFIC016000&query=feedbooks&__cf_chl_tk=gYPlUiiegGu_76aROqmqa.QAE22II8zOT7kOvT.83e4-1768780847-1.0.1.1-SnvLGIFPItwiLbpeLpV6BTSPUK_7naInWLgIpUPSRpg',
          cFPWv: 'b',
          cITimeS: '1768780847',
          cTplC: 0,
          cTplV: 5,
          cTplB: '0',
          fa: '\/search?cat=FBFIC016000&query=feedbooks&__cf_chl_f_tk=gYPlUiiegGu_76aROqmqa.QAE22II8zOT7kOvT.83e4-1768780847-1.0.1.1-SnvLGIFPItwiLbpeLpV6BTSPUK_7naInWLgIpUPSRpg',
          md: 'LpwQFvkdry2f7iNoXaMh4FdU4_zviUrYYRPDEmAauC0-1768780847-1.2.1.1-Nm0_E7OB1Oal1JtX7kxsf4IcKKxcwupr9UHd6bYXnVh4m8W3PetRhjszcBg6O4a9Mm79mLcElj_PHpgn8v5HVh2h5GyY497j1AZNphkphmCD3TmfHMRwRQ1Xzw5.ppa0AfXIGW3cC4htU6ZXPcjJsQEu8e_AEYok3rpOIIgoLXI3rgs6zIPRxmBf85oezuhIyufZCerFRQghvaPk5FM2yP4Df3Wn5ZiUoF6Fjkv9rePBwZp.idnhuMDSBK2issERYRm9qcVN0N.NHuG5KeQNupqEjecdmqUZNYMza_4NeFN4.wLyYLQPYhnYyXUShBYhLnz9x6.EooHjBtoGlcjHxBstaTd795EeXKlQYgu0MiZrKQu2RZtQuJiZoZTqEAPMh7OkF415yFsq.sBnGtjX2AT.qvpuj476h2aeX7xVJ7XQeK82Dl0Sr4sCQIZV01.gN9fAefSOqm5rrTb2LlV3T4OMNETn0AzVsiC8h17F2iT6QtwU7xvcMQhM9iQDywuVZ6xr04AIYc8DxNoA91ccumH7DFqOaC.t0YvGWIes6nNKnfMF89geo3d8LheC21eVSWL0F_iIMlU_tdysIQdq1XSktwG2lnK8xQuWv_g5QWb27tIF3N49f4jZy7v1B0VrH_Q.r1w5Mts6sr0nSLiTCE0Jvswzqseo9eMU09OPZBJxBaPlA3_xqS8bAsER76rngWD4IqamXpoOHeQExQGK1wgGPTlWnz_hkOks0Ys4mDjYLlBkG8iG35W4INzr2lPoE4tfllwFqp1lZQTVw51NFk4PUmvPP10ysF1URAU45FDp3y1gvDefVkBXMx_gY3NeguVLZe8f2s0wfs4OLiKvKrc_x5MeW1.qR8LnAxXvVHH2wMYXepEx55HXTjUcBlv7wha.Z_TjTMpdBBWmwV8chFZBSqFT.knk6Rqtf2GhnHuYWr42.s3gC.nyc5xxrWy9k93tbuv9cwjtDuMBnYarTR_qnuA_GPt0hlGnGCQAPXU8w.F6QSrD1GY1dRV9M_ho',
          mdrd: 'd2vw24jhAHV6tcAY9kNyZQzBsrcEVhnzIMiwalV18ms-1768780847-1.2.1.1-RQa2uzP6qTN6VIeSX9xNYBxxatUkkCardE1h8jgXxDQtK7tPdsGe.3BpmUvJTJbz4pcRKoTk68gHCZNcMcljtocnQOvUJ39F2_tj6zeOJ4Cqrr.RDKPK8kSNudpTH_Hvg9e2QdV5l_vVKXiTNkDCJXmZUw0SxUxo.PX5vZQygSXf3hNmRlE5DTNGyLB6JJV7oo1jLH0bmGIY4NYVI17moJ7SqdYhsod_U2VsEmmXsmsHwtiHuS.h0BDr60TpTCLtS_TP5R9l9fW7WIBofKi2Ulqj_4n1UGiA5y2IulrATDvgBtQMJscpaM5FUwzPv9WTgo5n76WzZjlkLHe7kbDgjvbP.2xXIaGjM0aWJwJ9_Dv8y8C9yrWGgEYKbGbaU_vAy3E60OM8089c.IaA445k4oOFvMXGnpm89wyAyxM0P33opKVp165jb25547QPN.703XqNFvFBlNkD_dH.PKinhi7UzcC0WfkeSm2VAFuVUVFjEg8.2UbnaPKBv339VLr3IXgnl3tpjoKYbEKy91jYN5Jls8WUQCNBtMblLIvd12.DOvgTRIhjlGOm6MTTvcdkz5c3r47zEoC2SeNFtjWOenV.J5tuQm.fRCmnw8dReLOoRkxONuKy04X3Vz7cDbdr2I4TJqZ2cHDZ5Ro0QQyuj69wkfZ_UF.Y08MX1AgNgFkBF.QQ5KdANOxsR_Z_akkgh3segQhNTpZNKLC_P.DAeZjrcvCqMfkg5e3EYKHICK_4J1JM29DQbW9JrX7gmvoOABq_fBvhq1t2iom_51aVSdWL7j1HSXnCgSjJUEQsezR0q.pLZzSVxbbDGRrf0w0m02UV2bKC6Mws0.alSR.5nHRbNMcB66KO_FH9bOsWUl_JbMcJtax.fSN0dHPhiO9S4_izDM3g_rhb8NKs9fK8Zp_44OiXKlGqa.ow0RaRLzVfuP.SwlcBmE6lox5iWZjb1gpyqspgqZSoYiDi4Qy9snTjbawXHx8Fbe86mzPdoRCeQkO4oOStz_hdjgSCjbd_0nXSlRlGiQyV8Yzy5KePxvoACJM94SIALN9LutmoJLWIzobjhu8KxfZ7Y2JsYg4sfaxdkkcPZzrMV2wlyuHxLk1Qli1KLeZy_8Ku57ZcFTXz7TyU9OEwnWuhfMozqhNvkmXhAKUMe3RdfQzMP4Zv100CDe50EIi0L.x7eCd6z6xyaPQkyV1vYSGJTb2.xSNfGKsrVIHUCYd4.tjT3MfFp7nxFjNQAwLDy3OCzZ9ZBAya6dutj0gNM70TySYkBw9Ehsey1KrGAaB_PhCIZDKzBxxBAa7QXVvtfYbOdhJ4iG1r1bcHpUsfB26NMJF83YMQgEbJyw4troBHfh4.tqL.UyU5BoLomoxMDoN9sBQ6bi76h85QB9_SDOpviCiuf21Khf8H.HKfTmc1XQGJpUx8urUA0gV4rydnv.m04C07ZiCvAq.rtgUYPhYMuGdbUBR4HRtnbcjc.uktZ6uZsPZn1DNgvfClPqGWYFhx72CiSzN44o3demz9L1PGr9VvbACqoXS6zFSfpJ94bns6u49FEI96WnakKq8I_26YY.tzOhUnQo8abdbMSh9vSLTIzAeTkq5.GOaHs_MMvSi9D6jgcXnjr13sJwQwpReS7wR_AYEa1ibsVDZ09kheEaAvd8dMgU5u9Xrq4g9as6s90ZASIurhJGuuKp8hg9a8gSYpcPdOh9E.N3m.sJuFFNfkra1XRTMiAWvs31Egk9VxcehfZYuwWhLI3aNoG7WdZGzlpBMX_Umgib_IXEMGwVnkyqWkuUN3oldOM_6casMxlZPKVdbU4Wh.YXC5hjeeurkgucUZPxx_1fPLAipSq6RJfFqjRkg5CMgZ2Kb7CeG1MFCv1YTGxJ4p4IxloQtaEFDk8eJOkwMg9JbHdxTnqkAWK91ofebTEQlUqfrTYF6bWVtArBQ.y7lVMAj2xQo5ULJMflnD6GnPdWdCOB0ezn.d_ydZXIv27sEC1H8OfnxoIQewulWg8NmtPM5qqMfGUKYiTYwVCtoA1aULoTSMsVt2Pfi_atINe9hMn.mN0iMAK6xG9nulVWbjrQM4AAMJUlktPulgmzOKiJU1Er4CWKNiwk11HYhFSQax_IV.Fq99bkRrcIbNhaC1iGFbJwX89No4ueAJO87j3CM21TehQ62k8818QXMQGEiqRtYjesYWwgr8CmO9dez_eBBdefXbONbFNIizcDPTFY8apsdbySTu2uMTtpSZJzUEsqnOIt22HP_RioFKarFq0fM8XTFtjRoctuD4Y0pC0SUBEJM2IDbDukqWUpoH_5Sx_Jk4wjQE1qn02u76uU4EN_8v868FiquaA0rjunUWKmp.xgX4iivwFcVgO.LF.MITzZ7CWkdE4tA7QbX_lFHvJswccZPVoft4c.I',
        };
        var a = document.createElement('script');
        a.src =
          '/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page/v1?ray=9c020dc7cece3e7e';
        window._cf_chl_opt.cOgUHash =
          location.hash === '' && location.href.indexOf('#') !== -1
            ? '#'
            : location.hash;
        window._cf_chl_opt.cOgUQuery =
          location.search === '' &&
          location.href
            .slice(0, location.href.length - window._cf_chl_opt.cOgUHash.length)
            .indexOf('?') !== -1
            ? '?'
            : location.search;
        if (window.history && window.history.replaceState) {
          var ogU =
            location.pathname +
            window._cf_chl_opt.cOgUQuery +
            window._cf_chl_opt.cOgUHash;
          history.replaceState(
            null,
            null,
            '\/search?cat=FBFIC016000&query=feedbooks&__cf_chl_rt_tk=gYPlUiiegGu_76aROqmqa.QAE22II8zOT7kOvT.83e4-1768780847-1.0.1.1-SnvLGIFPItwiLbpeLpV6BTSPUK_7naInWLgIpUPSRpg' +
              window._cf_chl_opt.cOgUHash
          );
          a.onload = function () {
            history.replaceState(null, null, ogU);
          };
        }
        document.getElementsByTagName('head')[0].appendChild(a);
      })();
    </script>
  </body>
</html>

(using-python-for-automation-1) Mac:request_and_parse_html_code vanessatsanguk$
```

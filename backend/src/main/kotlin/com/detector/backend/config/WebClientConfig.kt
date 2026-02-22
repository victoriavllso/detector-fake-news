import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.reactive.function.client.WebClient
import io.github.cdimascio.dotenv.dotenv


@Configuration
class WebClientConfig {
    @Bean
    fun webClient(builder: WebClient.Builder): WebClient {
        val dotenv = dotenv()
        return builder
        .baseUrl(dotenv["URL_MODEL"])
        .build()

    }
}

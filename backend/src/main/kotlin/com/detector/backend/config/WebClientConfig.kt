import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.reactive.function.client.WebClient

@Configuration
class WebClientConfig {
    @Bean
    fun webClient(builder: WebClient.Builder): WebClient = builder
        .baseUrl("https://api.example.com") // Set a default base URL (onde o ml vai rodar)
        .build()
}
